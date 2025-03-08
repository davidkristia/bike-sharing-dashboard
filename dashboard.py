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
    
    st.subheader("Visualisasi Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x="dteday", y="cnt", ax=ax)
    ax.set_title("Jumlah Peminjaman Sepeda per Hari")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)
else:
    st.warning("Tidak ada data untuk ditampilkan.")
