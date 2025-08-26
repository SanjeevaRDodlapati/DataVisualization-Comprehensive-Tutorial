
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #262730;
    }
</style>
""", unsafe_allow_html=True)

# Sample data generation (same as in notebook)
@st.cache_data
def load_sales_data():
    np.random.seed(42)
    dates = pd.date_range('2023-01-01', '2024-12-31', freq='D')
    n_days = len(dates)
    
    trend = np.linspace(1000, 1500, n_days)
    seasonality = 200 * np.sin(2 * np.pi * np.arange(n_days) / 365.25)
    weekly_pattern = 100 * np.sin(2 * np.pi * np.arange(n_days) / 7)
    noise = np.random.normal(0, 50, n_days)
    
    sales_data = pd.DataFrame({
        'date': dates,
        'sales': trend + seasonality + weekly_pattern + noise,
        'region': np.random.choice(['North', 'South', 'East', 'West'], n_days),
        'product': np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], n_days),
        'sales_rep': np.random.choice([f'Rep {i}' for i in range(1, 11)], n_days)
    })
    sales_data['sales'] = np.maximum(sales_data['sales'], 100)
    return sales_data

# Load data
df = load_sales_data()

# Header
st.markdown('<h1 class="main-header">📊 Sales Analytics Dashboard</h1>', unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("🔧 Filters & Controls")
st.sidebar.markdown("---")

# Date range selector
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[df['date'].min().date(), df['date'].max().date()],
    min_value=df['date'].min().date(),
    max_value=df['date'].max().date()
)

# Region selector
regions = st.sidebar.multiselect(
    "Select Regions",
    options=df['region'].unique(),
    default=df['region'].unique()
)

# Product selector
products = st.sidebar.multiselect(
    "Select Products",
    options=df['product'].unique(),
    default=df['product'].unique()
)

# Filter data based on selections
if len(date_range) == 2:
    filtered_df = df[
        (df['date'] >= pd.to_datetime(date_range[0])) &
        (df['date'] <= pd.to_datetime(date_range[1])) &
        (df['region'].isin(regions)) &
        (df['product'].isin(products))
    ]
else:
    filtered_df = df[
        (df['region'].isin(regions)) &
        (df['product'].isin(products))
    ]

# Key Metrics Row
st.subheader("📈 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df['sales'].sum()
avg_daily_sales = filtered_df['sales'].mean()
max_daily_sales = filtered_df['sales'].max()
total_days = len(filtered_df)

with col1:
    st.metric(
        label="Total Sales",
        value=f"${total_sales:,.0f}",
        delta=f"{total_sales/len(filtered_df)*30:,.0f} (30-day proj.)"
    )

with col2:
    st.metric(
        label="Average Daily Sales", 
        value=f"${avg_daily_sales:,.0f}",
        delta=f"{(avg_daily_sales-1200)/1200*100:+.1f}%"
    )

with col3:
    st.metric(
        label="Peak Daily Sales",
        value=f"${max_daily_sales:,.0f}",
        delta="Record high" if max_daily_sales > 1800 else "Within range"
    )

with col4:
    st.metric(
        label="Days in Period",
        value=f"{total_days:,}",
        delta=f"{total_days} days selected"
    )

# Charts Row 1
st.subheader("📊 Sales Trends Analysis")
col1, col2 = st.columns([2, 1])

with col1:
    # Time series chart
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    fig_ts = px.line(
        daily_sales, 
        x='date', 
        y='sales',
        title='Daily Sales Trend',
        color_discrete_sequence=['#1f77b4']
    )
    fig_ts.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        hovermode='x unified'
    )
    st.plotly_chart(fig_ts, use_container_width=True)

with col2:
    # Regional distribution
    regional_sales = filtered_df.groupby('region')['sales'].sum().reset_index()
    fig_pie = px.pie(
        regional_sales,
        values='sales',
        names='region',
        title='Sales by Region'
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    # Product performance
    product_sales = filtered_df.groupby('product')['sales'].agg(['sum', 'mean', 'count']).reset_index()
    product_sales.columns = ['product', 'total_sales', 'avg_sales', 'transaction_count']
    
    fig_bar = px.bar(
        product_sales,
        x='product',
        y='total_sales',
        title='Total Sales by Product',
        color='avg_sales',
        color_continuous_scale='viridis'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # Sales rep performance
    rep_performance = filtered_df.groupby('sales_rep')['sales'].agg(['sum', 'count']).reset_index()
    rep_performance.columns = ['sales_rep', 'total_sales', 'transaction_count']
    rep_performance = rep_performance.sort_values('total_sales', ascending=True).tail(10)
    
    fig_horizontal = px.bar(
        rep_performance,
        x='total_sales',
        y='sales_rep',
        orientation='h',
        title='Top 10 Sales Representatives',
        color='total_sales',
        color_continuous_scale='plasma'
    )
    st.plotly_chart(fig_horizontal, use_container_width=True)

# Advanced Analytics Section
st.subheader("🧪 Advanced Analytics")

# Moving averages
st.subheader("📈 Moving Average Analysis")
ma_days = st.slider("Moving Average Days", min_value=7, max_value=60, value=30)

daily_sales_ma = daily_sales.copy()
daily_sales_ma[f'MA_{ma_days}'] = daily_sales_ma['sales'].rolling(window=ma_days).mean()

fig_ma = go.Figure()
fig_ma.add_trace(go.Scatter(
    x=daily_sales_ma['date'],
    y=daily_sales_ma['sales'],
    mode='lines',
    name='Daily Sales',
    line=dict(color='lightblue', width=1),
    opacity=0.7
))
fig_ma.add_trace(go.Scatter(
    x=daily_sales_ma['date'],
    y=daily_sales_ma[f'MA_{ma_days}'],
    mode='lines',
    name=f'{ma_days}-Day Moving Average',
    line=dict(color='red', width=3)
))
fig_ma.update_layout(
    title=f'Sales Trend with {ma_days}-Day Moving Average',
    xaxis_title='Date',
    yaxis_title='Sales ($)'
)
st.plotly_chart(fig_ma, use_container_width=True)

# Data Table
st.subheader("📋 Detailed Data")
if st.checkbox("Show raw data"):
    st.dataframe(
        filtered_df.head(100),
        use_container_width=True
    )

# Summary statistics
st.subheader("📊 Summary Statistics")
col1, col2 = st.columns(2)

with col1:
    st.write("**Sales Statistics**")
    st.write(filtered_df['sales'].describe())

with col2:
    st.write("**Regional Breakdown**")
    regional_stats = filtered_df.groupby('region')['sales'].agg(['count', 'mean', 'std']).round(2)
    st.write(regional_stats)

# Footer
st.markdown("---")
st.markdown("**Dashboard Created with Streamlit** | Last Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
