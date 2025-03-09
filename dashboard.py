import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.title("Bike Sharing Dashboard")

# Load dataset dengan path relatif
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("main_data.csv")
        df["dteday"] = pd.to_datetime(df["dteday"])
        return df
    except FileNotFoundError:
        st.error("File dataset tidak ditemukan. Pastikan 'main_data.csv' ada dalam direktori yang benar.")
        return None

df = load_data()

if df is not None:
    st.subheader("Preview Data")
    st.write(df.head())
    
    st.subheader("Statistik Data")
    st.write(df.describe())
    
    st.sidebar.subheader("Filter Data")
    season_option = st.sidebar.selectbox("Pilih Musim:", sorted(df["season"].unique()))
    filtered_data = df[df["season"] == season_option]
    
    st.write(f"### Data untuk Musim {season_option}")
    st.write(filtered_data.head())
    
    # Visualisasi
    st.subheader("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax)
    ax.set_title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(fig)
    
    st.subheader("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x='temp', y='cnt', data=df, alpha=0.5, ax=ax)
    ax.set_title('Hubungan Suhu dengan Jumlah Penyewaan Sepeda')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    st.pyplot(fig)
    
    st.subheader("Distribusi Kelembapan Udara")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(df["hum"], bins=30, kde=True, color="purple", ax=ax)
    ax.set_title("Distribusi Kelembapan Udara")
    ax.set_xlabel("Kelembapan")
    ax.set_ylabel("Frekuensi")
    st.pyplot(fig)
else:
    st.warning("Tidak ada data untuk ditampilkan.")
