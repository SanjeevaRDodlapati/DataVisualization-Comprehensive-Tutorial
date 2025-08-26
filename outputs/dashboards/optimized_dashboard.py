
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import time

# Configure page with performance settings
st.set_page_config(
    page_title="Optimized Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Performance monitoring
@st.cache_data
def generate_large_dataset(n_samples=10000):
    """Generate large dataset with caching"""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        n_clusters_per_class=1,
        random_state=42
    )
    
    feature_names = [f'feature_{i}' for i in range(20)]
    df = pd.DataFrame(X, columns=feature_names)
    df['target'] = y
    df['category'] = np.random.choice(['A', 'B', 'C'], n_samples)
    
    return df

@st.cache_data
def compute_pca_analysis(data, n_components=2):
    """Cached PCA computation"""
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(data_scaled)
    
    return pca_result, pca.explained_variance_ratio_

@st.cache_data
def filter_data(df, selected_categories, feature_range):
    """Cached data filtering"""
    filtered_df = df[df['category'].isin(selected_categories)]
    
    # Apply feature range filtering if provided
    if feature_range:
        for feature, (min_val, max_val) in feature_range.items():
            filtered_df = filtered_df[
                (filtered_df[feature] >= min_val) & 
                (filtered_df[feature] <= max_val)
            ]
    
    return filtered_df

# Initialize session state
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'analysis_cache' not in st.session_state:
    st.session_state.analysis_cache = {}

# Title and description
st.title("⚡ High-Performance Dashboard")
st.markdown("**Demonstration of optimized Streamlit techniques for large datasets**")

# Performance metrics in sidebar
st.sidebar.header("📊 Performance Metrics")

# Data loading with progress
if not st.session_state.data_loaded:
    with st.spinner("Loading dataset..."):
        start_time = time.time()
        df = generate_large_dataset(10000)
        load_time = time.time() - start_time
        st.session_state.data_loaded = True
        st.session_state.df = df
        st.sidebar.success(f"Data loaded in {load_time:.2f}s")
else:
    df = st.session_state.df
    st.sidebar.info("Data loaded from cache")

# Sidebar controls
st.sidebar.header("🔧 Controls")

# Category filter
selected_categories = st.sidebar.multiselect(
    "Select Categories",
    options=['A', 'B', 'C'],
    default=['A', 'B', 'C'],
    key="category_filter"
)

# Feature selection
feature_columns = [col for col in df.columns if col.startswith('feature_')]
selected_features = st.sidebar.multiselect(
    "Select Features for Analysis",
    options=feature_columns,
    default=feature_columns[:5],
    key="feature_selection"
)

# Analysis type
analysis_type = st.sidebar.selectbox(
    "Analysis Type",
    ["Overview", "PCA Analysis", "Feature Correlation"],
    key="analysis_type"
)

# Only filter data when selections change
filter_key = f"{tuple(selected_categories)}_{tuple(selected_features)}"
if filter_key not in st.session_state.analysis_cache:
    with st.spinner("Filtering data..."):
        start_time = time.time()
        filtered_df = filter_data(df, selected_categories, None)
        filter_time = time.time() - start_time
        st.session_state.analysis_cache[filter_key] = filtered_df
        st.sidebar.info(f"Filter time: {filter_time:.3f}s")
else:
    filtered_df = st.session_state.analysis_cache[filter_key]
    st.sidebar.info("Filtered data from cache")

# Display metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Records", f"{len(df):,}")
with col2:
    st.metric("Filtered Records", f"{len(filtered_df):,}")
with col3:
    st.metric("Selected Features", len(selected_features))
with col4:
    st.metric("Cache Entries", len(st.session_state.analysis_cache))

# Main content based on analysis type
if analysis_type == "Overview":
    st.subheader("📊 Dataset Overview")
    
    # Use columns for efficient layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Category distribution
        category_counts = filtered_df['category'].value_counts()
        fig_pie = px.pie(
            values=category_counts.values,
            names=category_counts.index,
            title="Category Distribution"
        )
        st.plotly_chart(fig_pie, use_container_width=True, key="category_pie")
    
    with col2:
        # Target distribution
        target_counts = filtered_df['target'].value_counts()
        fig_bar = px.bar(
            x=target_counts.index,
            y=target_counts.values,
            title="Target Distribution"
        )
        st.plotly_chart(fig_bar, use_container_width=True, key="target_bar")

elif analysis_type == "PCA Analysis":
    if len(selected_features) >= 2:
        st.subheader("🎯 Principal Component Analysis")
        
        # Cached PCA computation
        pca_key = f"pca_{filter_key}_{tuple(selected_features)}"
        if pca_key not in st.session_state.analysis_cache:
            with st.spinner("Computing PCA..."):
                start_time = time.time()
                pca_result, variance_ratio = compute_pca_analysis(
                    filtered_df[selected_features], 
                    n_components=min(3, len(selected_features))
                )
                pca_time = time.time() - start_time
                st.session_state.analysis_cache[pca_key] = (pca_result, variance_ratio)
                st.sidebar.info(f"PCA time: {pca_time:.3f}s")
        else:
            pca_result, variance_ratio = st.session_state.analysis_cache[pca_key]
            st.sidebar.info("PCA from cache")
        
        # Explained variance
        col1, col2 = st.columns(2)
        
        with col1:
            variance_df = pd.DataFrame({
                'Component': [f'PC{i+1}' for i in range(len(variance_ratio))],
                'Explained_Variance': variance_ratio
            })
            fig_var = px.bar(
                variance_df,
                x='Component',
                y='Explained_Variance',
                title='Explained Variance by Component'
            )
            st.plotly_chart(fig_var, use_container_width=True)
        
        with col2:
            # PCA scatter plot
            pca_df = pd.DataFrame(pca_result[:, :2], columns=['PC1', 'PC2'])
            pca_df['category'] = filtered_df['category'].values
            pca_df['target'] = filtered_df['target'].values
            
            fig_pca = px.scatter(
                pca_df,
                x='PC1',
                y='PC2',
                color='category',
                symbol='target',
                title='PCA Visualization'
            )
            st.plotly_chart(fig_pca, use_container_width=True)
    else:
        st.warning("Please select at least 2 features for PCA analysis")

else:  # Feature Correlation
    if len(selected_features) >= 2:
        st.subheader("🔗 Feature Correlation Analysis")
        
        # Cached correlation computation
        corr_key = f"corr_{filter_key}_{tuple(selected_features)}"
        if corr_key not in st.session_state.analysis_cache:
            with st.spinner("Computing correlations..."):
                start_time = time.time()
                correlation_matrix = filtered_df[selected_features].corr()
                corr_time = time.time() - start_time
                st.session_state.analysis_cache[corr_key] = correlation_matrix
                st.sidebar.info(f"Correlation time: {corr_time:.3f}s")
        else:
            correlation_matrix = st.session_state.analysis_cache[corr_key]
            st.sidebar.info("Correlation from cache")
        
        # Correlation heatmap
        fig_corr = px.imshow(
            correlation_matrix,
            text_auto=True,
            aspect="auto",
            title="Feature Correlation Matrix"
        )
        st.plotly_chart(fig_corr, use_container_width=True)
    else:
        st.warning("Please select at least 2 features for correlation analysis")

# Performance summary
st.sidebar.markdown("---")
st.sidebar.subheader("⚡ Performance Summary")
st.sidebar.info(f"Cache size: {len(st.session_state.analysis_cache)} entries")
st.sidebar.info(f"Total records: {len(df):,}")

# Clear cache button
if st.sidebar.button("Clear Cache"):
    st.session_state.analysis_cache.clear()
    st.sidebar.success("Cache cleared!")
