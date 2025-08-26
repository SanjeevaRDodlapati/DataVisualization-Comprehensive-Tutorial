
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.datasets import load_iris, load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns

st.set_page_config(
    page_title="Scientific Data Explorer",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Scientific Data Explorer")
st.markdown("**Interactive analysis of scientific datasets with machine learning insights**")

# Sidebar for dataset selection
st.sidebar.header("🧪 Dataset Selection")
dataset_choice = st.sidebar.selectbox(
    "Choose a dataset:",
    ["Iris Flower Dataset", "Wine Quality Dataset"]
)

@st.cache_data
def load_scientific_data(dataset_name):
    if dataset_name == "Iris Flower Dataset":
        data = load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['target'] = data.target
        df['species'] = [data.target_names[i] for i in data.target]
        return df, data.feature_names, 'species'
    else:  # Wine dataset
        data = load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['target'] = data.target
        df['wine_class'] = [f'Class {i}' for i in data.target]
        return df, data.feature_names, 'wine_class'

df, feature_names, target_col = load_scientific_data(dataset_choice)

# Analysis options
st.sidebar.header("🔍 Analysis Options")
analysis_type = st.sidebar.selectbox(
    "Select Analysis Type:",
    ["Exploratory Data Analysis", "Principal Component Analysis", "Clustering Analysis", "Feature Relationships"]
)

if analysis_type == "Exploratory Data Analysis":
    st.header("📊 Exploratory Data Analysis")
    
    # Dataset overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Samples", len(df))
    with col2:
        st.metric("Features", len(feature_names))
    with col3:
        st.metric("Classes", df[target_col].nunique())
    
    # Feature selection for visualization
    selected_features = st.multiselect(
        "Select features to analyze:",
        feature_names,
        default=feature_names[:4] if len(feature_names) >= 4 else feature_names
    )
    
    if selected_features:
        # Distribution plots
        st.subheader("📈 Feature Distributions")
        fig_dist = make_subplots(
            rows=2, cols=2,
            subplot_titles=selected_features[:4],
            specs=[[{"type": "xy"}, {"type": "xy"}],
                   [{"type": "xy"}, {"type": "xy"}]]
        )
        
        for i, feature in enumerate(selected_features[:4]):
            row = i // 2 + 1
            col = i % 2 + 1
            
            for class_name in df[target_col].unique():
                class_data = df[df[target_col] == class_name][feature]
                fig_dist.add_trace(
                    go.Histogram(
                        x=class_data,
                        name=f"{class_name}",
                        opacity=0.7,
                        legendgroup=class_name,
                        showlegend=(i == 0)
                    ),
                    row=row, col=col
                )
        
        fig_dist.update_layout(
            title="Feature Distributions by Class",
            height=600,
            barmode='overlay'
        )
        st.plotly_chart(fig_dist, use_container_width=True)
        
        # Correlation matrix
        st.subheader("🔗 Feature Correlation Matrix")
        corr_matrix = df[selected_features].corr()
        
        fig_corr = px.imshow(
            corr_matrix,
            text_auto=True,
            aspect="auto",
            title="Feature Correlation Heatmap",
            color_continuous_scale="RdBu"
        )
        st.plotly_chart(fig_corr, use_container_width=True)

elif analysis_type == "Principal Component Analysis":
    st.header("🎯 Principal Component Analysis")
    
    # PCA computation
    X = df[feature_names]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    n_components = st.slider("Number of PCA Components", 2, min(len(feature_names), 10), 3)
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    # Explained variance
    st.subheader("📊 Explained Variance")
    variance_df = pd.DataFrame({
        'Component': [f'PC{i+1}' for i in range(n_components)],
        'Explained_Variance': pca.explained_variance_ratio_,
        'Cumulative_Variance': np.cumsum(pca.explained_variance_ratio_)
    })
    
    fig_var = px.bar(
        variance_df,
        x='Component',
        y='Explained_Variance',
        title='Explained Variance by Principal Component'
    )
    st.plotly_chart(fig_var, use_container_width=True)
    
    # PCA scatter plot
    st.subheader("🎨 PCA Visualization")
    if n_components >= 2:
        pca_df = pd.DataFrame(X_pca[:, :3], columns=[f'PC{i+1}' for i in range(min(3, n_components))])
        pca_df[target_col] = df[target_col]
        
        if n_components >= 3:
            fig_3d = px.scatter_3d(
                pca_df,
                x='PC1',
                y='PC2',
                z='PC3',
                color=target_col,
                title='3D PCA Visualization'
            )
            st.plotly_chart(fig_3d, use_container_width=True)
        
        fig_2d = px.scatter(
            pca_df,
            x='PC1',
            y='PC2',
            color=target_col,
            title='2D PCA Visualization'
        )
        st.plotly_chart(fig_2d, use_container_width=True)

elif analysis_type == "Clustering Analysis":
    st.header("🎯 K-Means Clustering Analysis")
    
    # Feature selection for clustering
    clustering_features = st.multiselect(
        "Select features for clustering:",
        feature_names,
        default=feature_names[:4] if len(feature_names) >= 4 else feature_names
    )
    
    if clustering_features:
        X_cluster = df[clustering_features]
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_cluster)
        
        # Number of clusters
        n_clusters = st.slider("Number of Clusters", 2, 10, 3)
        
        # Perform clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(X_scaled)
        
        # Add cluster labels to dataframe
        df_clustered = df.copy()
        df_clustered['Cluster'] = [f'Cluster {i}' for i in cluster_labels]
        
        # Visualization
        if len(clustering_features) >= 2:
            fig_cluster = px.scatter(
                df_clustered,
                x=clustering_features[0],
                y=clustering_features[1],
                color='Cluster',
                symbol=target_col,
                title=f'K-Means Clustering (k={n_clusters})',
                hover_data=clustering_features[2:] if len(clustering_features) > 2 else None
            )
            st.plotly_chart(fig_cluster, use_container_width=True)
        
        # Cluster centers
        st.subheader("🎯 Cluster Centers")
        centers_df = pd.DataFrame(
            scaler.inverse_transform(kmeans.cluster_centers_),
            columns=clustering_features,
            index=[f'Cluster {i}' for i in range(n_clusters)]
        )
        st.dataframe(centers_df, use_container_width=True)

else:  # Feature Relationships
    st.header("🔗 Feature Relationships Analysis")
    
    # Feature selection
    col1, col2 = st.columns(2)
    with col1:
        x_feature = st.selectbox("Select X-axis feature:", feature_names)
    with col2:
        y_feature = st.selectbox("Select Y-axis feature:", feature_names, index=1)
    
    # Scatter plot with regression
    fig_scatter = px.scatter(
        df,
        x=x_feature,
        y=y_feature,
        color=target_col,
        trendline="ols",
        title=f'{x_feature} vs {y_feature}',
        hover_data=feature_names
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Statistical summary
    st.subheader("📊 Statistical Summary")
    correlation = df[x_feature].corr(df[y_feature])
    st.metric("Pearson Correlation", f"{correlation:.3f}")
    
    # Box plots
    st.subheader("📦 Distribution by Class")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_box1 = px.box(df, x=target_col, y=x_feature, title=f'{x_feature} by Class')
        st.plotly_chart(fig_box1, use_container_width=True)
    
    with col2:
        fig_box2 = px.box(df, x=target_col, y=y_feature, title=f'{y_feature} by Class')
        st.plotly_chart(fig_box2, use_container_width=True)

# Raw data display
st.sidebar.markdown("---")
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("📋 Raw Dataset")
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("**Scientific Data Explorer** | Built with Streamlit & Scikit-learn")
