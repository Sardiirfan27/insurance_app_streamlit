# visualization.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# Load Data
# =====================
@st.cache_data
def load_data():
    df = pd.read_csv("./data/insurance.csv")
    return df

df = load_data()

# =====================
# Page Layout
# =====================
st.set_page_config(
    page_title="Insurance Data Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Insurance Dataset Visualization")
st.markdown("Visualisasi data **insurance.csv** dengan Streamlit.")

# =====================
# Sidebar Filters
# =====================
st.sidebar.header("Filter Options")

regions = st.sidebar.multiselect(
    "Pilih Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

smoker_filter = st.sidebar.multiselect(
    "Pilih Status Perokok",
    options=df["smoker"].unique(),
    default=df["smoker"].unique()
)

filtered_df = df[
    (df["region"].isin(regions)) &
    (df["smoker"].isin(smoker_filter))
]

st.sidebar.markdown(f"Jumlah data terfilter: **{len(filtered_df)}**")

# =====================
# Layout 2 Kolom
# =====================
col1, col2 = st.columns(2)

# --- Distribusi Umur ---
with col1:
    st.subheader("Distribusi Umur")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(filtered_df["age"], bins=15, kde=True, ax=ax)
    st.pyplot(fig)

# --- Rata-rata Charges per Region ---
with col2:
    st.subheader("Rata-rata Charges per Region")
    mean_charges = filtered_df.groupby("region")["charges"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x="region", y="charges", data=mean_charges, ax=ax)
    st.pyplot(fig)

# =====================
# Layout 2 Kolom Lagi
# =====================
col3, col4 = st.columns(2)

# --- Boxplot Charges vs Smoker ---
with col3:
    st.subheader("Charges berdasarkan Status Perokok")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.boxplot(x="smoker", y="charges", data=filtered_df, ax=ax)
    st.pyplot(fig)

# --- Scatter Plot BMI vs Charges ---
with col4:
    st.subheader("BMI vs Charges")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        x="bmi", y="charges",
        hue="smoker", data=filtered_df, ax=ax
    )
    st.pyplot(fig)

# =====================
# Tampilkan Dataframe
# =====================
st.subheader("📄 Dataframe Hasil Filter")
st.dataframe(filtered_df)
