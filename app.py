import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm

st.set_page_config(page_title="ShopEase Analytics Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('shopease_cleaned.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'], errors='coerce')
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

city_filter = st.sidebar.multiselect("City", options=sorted(df['City'].unique()), default=sorted(df['City'].unique()))
category_filter = st.sidebar.multiselect("Category", options=sorted(df['Category'].unique()), default=sorted(df['Category'].unique()))
gender_filter = st.sidebar.multiselect("Gender", options=sorted(df['Gender'].unique()), default=sorted(df['Gender'].unique()))
status_filter = st.sidebar.multiselect("Order Status", options=sorted(df['Order Status'].unique()), default=sorted(df['Order Status'].unique()))

age_range = st.sidebar.slider("Customer Age", int(df['Customer Age'].min()), int(df['Customer Age'].max()), (18, 80))
price_range = st.sidebar.slider("Unit Price", float(df['Unit Price'].min()), float(df['Unit Price'].max()), (float(df['Unit Price'].min()), float(df['Unit Price'].max())))

# Apply filters
filtered = df[
    (df['City'].isin(city_filter)) &
    (df['Category'].isin(category_filter)) &
    (df['Gender'].isin(gender_filter)) &
    (df['Order Status'].isin(status_filter)) &
    (df['Customer Age'].between(age_range[0], age_range[1])) &
    (df['Unit Price'].between(price_range[0], price_range[1]))
]

# Header
st.title("🛍️ ShopEase Dynamic Analytical Dashboard")
st.markdown(f"**Filtered Records:** {len(filtered)} / {len(df)}")

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered['Total Amount'].sum():,.0f}")
col2.metric("Total Orders", f"{len(filtered):,}")
col3.metric("Avg Order Value", f"${filtered['Total Amount'].mean():,.2f}")
col4.metric("Avg Rating", f"{filtered['Rating'].mean():.2f} ⭐")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Visualizations", "📈 Statistics", "🔬 Inferential Tests", "📋 Data"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Revenue by Category")
        fig, ax = plt.subplots()
        filtered.groupby('Category')['Total Amount'].sum().plot(kind='bar', ax=ax, color='teal')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.subheader("Orders by City")
        fig, ax = plt.subplots()
        filtered['City'].value_counts().plot(kind='bar', ax=ax, color='coral')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Total Amount Distribution")
        fig, ax = plt.subplots()
        sns.histplot(filtered['Total Amount'], bins=40, kde=True, ax=ax, color='purple')
        st.pyplot(fig)

    with col4:
        st.subheader("Boxplot: Amount by Category")
        fig, ax = plt.subplots()
        sns.boxplot(x='Category', y='Total Amount', data=filtered, ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Rating Distribution")
        fig, ax = plt.subplots()
        sns.countplot(x='Rating', data=filtered, ax=ax, palette='viridis')
        st.pyplot(fig)

    with col6:
        st.subheader("Correlation Heatmap")
        numeric_cols = ['Customer Age', 'Quantity', 'Unit Price', 'Discount', 'Rating', 'Total Amount']
        fig, ax = plt.subplots()
        sns.heatmap(filtered[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
        st.pyplot(fig)

    st.subheader("Scatter: Unit Price vs Total Amount")
    fig, ax = plt.subplots()
    sns.scatterplot(x='Unit Price', y='Total Amount', hue='Category', data=filtered, alpha=0.6, ax=ax)
    st.pyplot(fig)

with tab2:
    st.subheader("Descriptive Statistics")
    numeric_cols = ['Customer Age', 'Quantity', 'Unit Price', 'Discount', 'Rating', 'Total Amount']
    st.dataframe(filtered[numeric_cols].describe())

    st.subheader("Categorical Summary")
    for col in ['Gender', 'City', 'Category', 'Payment Method', 'Order Status']:
        st.write(f"**{col}:**")
        st.dataframe(filtered[col].value_counts().reset_index().rename(columns={'index': col, col: 'Count'}))

with tab3:
    st.subheader("Hypothesis Tests")

    if len(filtered) > 10:
        male = filtered[filtered['Gender'] == 'Male']['Total Amount']
        female = filtered[filtered['Gender'] == 'Female']['Total Amount']
        if len(male) > 2 and len(female) > 2:
            t_stat, p_val = stats.ttest_ind(male, female)
            st.write(f"**t-test (Gender vs Total Amount):** t = {t_stat:.3f}, p = {p_val:.4f}")
            if p_val < 0.05:
                st.success("Reject H₀: Significant difference between genders.")
            else:
                st.info("Fail to reject H₀: No significant difference.")

        cats = [g['Total Amount'].values for _, g in filtered.groupby('Category')]
        if len(cats) > 1:
            f_stat, p_val = stats.f_oneway(*cats)
            st.write(f"**ANOVA (Category vs Total Amount):** F = {f_stat:.3f}, p = {p_val:.4f}")

        contingency = pd.crosstab(filtered['Gender'], filtered['Order Status'])
        if contingency.shape[0] > 1 and contingency.shape[1] > 1:
            chi2, p, dof, _ = stats.chi2_contingency(contingency)
            st.write(f"**Chi-square (Gender vs Order Status):** χ² = {chi2:.3f}, p = {p:.4f}")

        pearson_r, pearson_p = stats.pearsonr(filtered['Unit Price'], filtered['Total Amount'])
        st.write(f"**Pearson Correlation (Unit Price vs Total Amount):** r = {pearson_r:.3f}, p = {pearson_p:.4f}")

with tab4:
    st.subheader("Filtered Data")
    st.dataframe(filtered)
    st.download_button("Download Filtered CSV", filtered.to_csv(index=False), "filtered_data.csv")
