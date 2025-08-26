
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configure the page
st.set_page_config(
    page_title="Multi-Page Dashboard",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Overview'

# Navigation
st.sidebar.title("📚 Navigation")
pages = {
    "📊 Overview": "Overview",
    "📈 Analytics": "Analytics", 
    "🎯 Predictions": "Predictions",
    "⚙️ Settings": "Settings"
}

selected_page = st.sidebar.radio("Go to:", list(pages.keys()))
st.session_state.page = pages[selected_page]

# Sample data
@st.cache_data
def generate_sample_data():
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=365, freq='D')
    data = pd.DataFrame({
        'date': dates,
        'metric_a': np.cumsum(np.random.randn(365)) + 100,
        'metric_b': np.cumsum(np.random.randn(365)) + 50,
        'category': np.random.choice(['X', 'Y', 'Z'], 365),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 365)
    })
    return data

df = generate_sample_data()

# Page content
if st.session_state.page == "Overview":
    st.title("📊 Dashboard Overview")
    st.markdown("Welcome to the multi-page interactive dashboard!")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Records", len(df), delta="365 days")
    with col2:
        st.metric("Avg Metric A", f"{df['metric_a'].mean():.1f}", delta="↑ 2.3%")
    with col3:
        st.metric("Avg Metric B", f"{df['metric_b'].mean():.1f}", delta="↓ 1.1%")
    with col4:
        st.metric("Categories", df['category'].nunique(), delta="3 active")
    
    # Overview charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig1 = px.line(df, x='date', y='metric_a', title='Metric A Trend')
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        category_counts = df['category'].value_counts()
        fig2 = px.pie(values=category_counts.values, names=category_counts.index, title='Category Distribution')
        st.plotly_chart(fig2, use_container_width=True)

elif st.session_state.page == "Analytics":
    st.title("📈 Advanced Analytics")
    
    # Filters
    st.sidebar.header("🔧 Filters")
    date_range = st.sidebar.date_input(
        "Date Range",
        value=[df['date'].min().date(), df['date'].max().date()],
        min_value=df['date'].min().date(),
        max_value=df['date'].max().date()
    )
    
    selected_categories = st.sidebar.multiselect(
        "Categories",
        df['category'].unique(),
        default=df['category'].unique()
    )
    
    # Filter data
    if len(date_range) == 2:
        filtered_df = df[
            (df['date'] >= pd.to_datetime(date_range[0])) &
            (df['date'] <= pd.to_datetime(date_range[1])) &
            (df['category'].isin(selected_categories))
        ]
    else:
        filtered_df = df[df['category'].isin(selected_categories)]
    
    # Analytics content
    tab1, tab2, tab3 = st.tabs(["📊 Trends", "🔍 Correlations", "📋 Statistics"])
    
    with tab1:
        fig = px.line(filtered_df, x='date', y=['metric_a', 'metric_b'], title='Metrics Over Time')
        st.plotly_chart(fig, use_container_width=True)
        
        # Regional analysis
        regional_data = filtered_df.groupby(['region', 'category']).agg({
            'metric_a': 'mean',
            'metric_b': 'mean'
        }).reset_index()
        
        fig_region = px.bar(
            regional_data, 
            x='region', 
            y='metric_a', 
            color='category',
            title='Average Metric A by Region and Category'
        )
        st.plotly_chart(fig_region, use_container_width=True)
    
    with tab2:
        # Correlation analysis
        correlation = filtered_df[['metric_a', 'metric_b']].corr()
        fig_corr = px.imshow(correlation, text_auto=True, title='Metric Correlation')
        st.plotly_chart(fig_corr, use_container_width=True)
        
        # Scatter plot
        fig_scatter = px.scatter(
            filtered_df, 
            x='metric_a', 
            y='metric_b', 
            color='category',
            title='Metric A vs Metric B'
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    with tab3:
        st.subheader("📊 Summary Statistics")
        st.dataframe(filtered_df[['metric_a', 'metric_b']].describe())
        
        st.subheader("📋 Sample Data")
        st.dataframe(filtered_df.head(20))

elif st.session_state.page == "Predictions":
    st.title("🎯 Predictive Analytics")
    st.info("This section would contain machine learning models and predictions.")
    
    # Simple moving average prediction
    window = st.slider("Moving Average Window", 5, 50, 20)
    
    df_pred = df.copy()
    df_pred['ma_metric_a'] = df_pred['metric_a'].rolling(window=window).mean()
    
    # Simple linear extrapolation for demo
    last_values = df_pred['metric_a'].tail(window).values
    trend = np.polyfit(range(window), last_values, 1)
    future_dates = pd.date_range(df['date'].max() + timedelta(days=1), periods=30, freq='D')
    future_values = [trend[0] * (window + i) + trend[1] for i in range(30)]
    
    # Combine historical and predicted
    pred_df = pd.DataFrame({
        'date': list(df['date']) + list(future_dates),
        'metric_a': list(df['metric_a']) + [np.nan] * 30,
        'predicted': [np.nan] * len(df) + future_values
    })
    
    fig_pred = go.Figure()
    fig_pred.add_trace(go.Scatter(
        x=pred_df['date'][:len(df)],
        y=pred_df['metric_a'][:len(df)],
        mode='lines',
        name='Historical',
        line=dict(color='blue')
    ))
    fig_pred.add_trace(go.Scatter(
        x=pred_df['date'][len(df):],
        y=pred_df['predicted'][len(df):],
        mode='lines',
        name='Predicted',
        line=dict(color='red', dash='dash')
    ))
    fig_pred.update_layout(title='Metric A: Historical vs Predicted')
    st.plotly_chart(fig_pred, use_container_width=True)

else:  # Settings
    st.title("⚙️ Dashboard Settings")
    
    # Theme settings
    st.subheader("🎨 Appearance")
    theme_color = st.color_picker("Primary Color", "#1f77b4")
    
    # Data settings
    st.subheader("📊 Data Configuration")
    refresh_rate = st.selectbox("Data Refresh Rate", ["Manual", "5 minutes", "15 minutes", "1 hour"])
    
    # Export settings
    st.subheader("📤 Export Options")
    export_format = st.selectbox("Default Export Format", ["CSV", "Excel", "JSON"])
    
    # Save settings
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
        
    # Reset button
    if st.button("Reset to Defaults"):
        st.warning("Settings reset to defaults.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Multi-Page Dashboard** | Built with Streamlit")
st.sidebar.markdown(f"Current time: {datetime.now().strftime('%H:%M:%S')}")
