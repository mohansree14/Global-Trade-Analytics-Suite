import streamlit as st
import pandas as pd
import plotly.express as px
from src.analysis import load_data, get_country_aggregates, get_monthly_trends
from src.model import train_model
from sklearn.metrics import mean_absolute_error
from src.generate_data import generate_data
import os

st.set_page_config(page_title="Global Trade Analytics", page_icon="🌍", layout="wide")

# Custom CSS for Premium UI
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stApp {
        background-color: #0e1117;
    }
    div[data-testid="stMetric"] {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #374151;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    div[data-testid="stMetric"] label {
        color: #9ca3af;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #f3f4f6;
        font-weight: 700;
    }
    h1 {
        color: #60a5fa;
        font-family: 'Inter', sans-serif;
    }
    h2, h3 {
        color: #e5e7eb;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #9ca3af;
    }
    .stTabs [aria-selected="true"] {
        background-color: transparent;
        border-bottom: 2px solid #60a5fa;
        color: #60a5fa;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 Global Trade Analytics Suite")
st.markdown("""
<div style='background-color: #1f2937; padding: 15px; border-radius: 10px; border-left: 5px solid #60a5fa; margin-bottom: 25px;'>
    <h4 style='color: #f3f4f6; margin:0;'>Market Intelligence Dashboard</h4>
    <p style='color: #d1d5db; margin:5px 0 0 0;'>
    Advanced platform for statistical modeling, geospatial trade analysis, and AI-driven forecasting.
    </p>
</div>
""", unsafe_allow_html=True)

# Load Data
data_path = 'data/global_trade_data.csv'

@st.cache_data
def get_data():
    if not os.path.exists(data_path):
        st.warning("Data repository empty. Initializing synthetic trade records...")
        try:
            df_gen = generate_data()
            os.makedirs('data', exist_ok=True)
            df_gen.to_csv(data_path, index=False)
            st.success("Database initialized successfully.")
            return df_gen
        except Exception as e:
            st.error(f"System Error: {e}")
            return pd.DataFrame()
    return load_data(data_path)

df = get_data()

if df.empty:
    st.stop()

# Sidebar Filters
st.sidebar.header("Configuration")
selected_year = st.sidebar.selectbox("Fiscal Year", sorted(df['Year'].unique(), reverse=True))
df_filtered = df[df['Year'] == selected_year]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Trade Volume", f"${df_filtered['Trade_Volume_USD'].sum()/1e9:,.2f}B", delta="1.2%")
col2.metric("Total Trade Weight", f"{df_filtered['Trade_Weight_KG'].sum()/1e6:,.2f}M KG", delta="-0.5%")
col3.metric("Transaction Count", f"{len(df_filtered):,}")

# Tabs
tab1, tab2, tab3 = st.tabs(["Geospatial Intelligence", "Market Trends", "AI Forecasting"])

with tab1:
    st.header("Global Trade Routes")
    st.markdown("Interactive analysis of international trade flow distributions.")
    
    country_stats = get_country_aggregates(df_filtered)
    
    # Choropleth Map
    # Enhanced Interactive 3D Globe
    fig_map = px.choropleth(
        country_stats,
        locations="Country",
        locationmode="country names",
        color="Total_Trade_Volume",
        hover_name="Country",
        hover_data={
            'Total_Trade_Volume': ':,.0f',
            'Total_Export_Volume': ':,.0f',
            'Total_Import_Volume': ':,.0f',
            'Country': False
        },
        color_continuous_scale="Viridis", # High contrast for dark theme
        title=f"Global Trade Volume Density ({selected_year})"
    )
    
    fig_map.update_layout(
        geo=dict(
            projection_type="orthographic",
            showocean=True,
            oceancolor="#0e1117", # Matches app background
            showlakes=True,
            lakecolor="#0e1117",
            showcoastlines=True,
            coastlinecolor="#374151",
            bgcolor='rgba(0,0,0,0)',
            showland=True,
            landcolor="#1f2937"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin={"r":0,"t":50,"l":0,"b":0},
        font=dict(color="#f3f4f6"),
        coloraxis_colorbar=dict(
            title="Volume (USD)",
            thicknessmode="pixels", thickness=15,
            lenmode="pixels", len=300,
            yanchor="top", y=1,
            ticks="outside", 
            tickfont=dict(color="#9ca3af")
        )
    )
    st.plotly_chart(fig_map, use_container_width=True)

with tab2:
    st.header("Temporal Market Analysis")
    st.markdown("Historical trade volume analysis identifying seasonal patterns and growth trends.")
    
    monthly_trend = get_monthly_trends(df)
    fig_trend = px.line(
        monthly_trend, 
        x='Date', 
        y='Trade_Volume_USD',
        title="Global Trade Volume Trend (All Years)",
        markers=True
    )
    fig_trend.update_layout(height=400)
    st.plotly_chart(fig_trend, use_container_width=True)
    
    st.subheader("Category Performance")
    fig_bar = px.bar(
        df_filtered.groupby('Product_Category')['Trade_Volume_USD'].sum().reset_index(),
        x='Product_Category',
        y='Trade_Volume_USD',
        color='Product_Category',
        title=f"Volume by Product Segment ({selected_year})"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab3:
    st.header("Predictive Modeling Engine")
    st.markdown("AI-driven forecasting utilizing Random Forest regression algorithms.")
    
    if st.button("Train Predictive Model"):
        with st.spinner("Optimizing Random Forest Regressor..."):
            model, r2, y_test, y_pred = train_model(df)
            
        st.success("Model Optimization Complete")
        
        c1, c2 = st.columns(2)
        c1.metric("Model Precision (R²)", f"{r2*100:.2f}%", delta="Optimized")
        c2.metric("MAE (Mean Absolute Error)", f"${mean_absolute_error(y_test, y_pred):,.2f}")
        
        if r2 >= 0.88:
            st.balloons()
        
        # Plot Actual vs Predicted
        results_df = pd.DataFrame({'Actual Volume': y_test, 'Predicted Volume': y_pred}).head(100)
        fig_pred = px.scatter(
            results_df, x='Actual Volume', y='Predicted Volume', 
            title="Model Validation: Actual vs Predicted Trade Volume",
            trendline="ols",
            color_discrete_sequence=['#60a5fa']
        )
        st.plotly_chart(fig_pred, use_container_width=True)
