import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.title("Bike Sharing Dashboard")

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
    st.sidebar.subheader("Filter Data")

    # Filter berdasarkan musim
    season_option = st.sidebar.selectbox("Pilih Musim:", sorted(df["season"].unique()))
    
    # Filter berdasarkan rentang tanggal
    min_date = df["dteday"].min().date()
    max_date = df["dteday"].max().date()
    date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)
    
    # Filter berdasarkan rentang suhu
    temp_range = st.sidebar.slider("Pilih Rentang Suhu", float(df["temp"].min()), float(df["temp"].max()), (float(df["temp"].min()), float(df["temp"].max())))

    # Terapkan filter
    filtered_data = df[(df["season"] == season_option) & 
                       (df["dteday"].between(pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1]))) & 
                       (df["temp"].between(temp_range[0], temp_range[1]))]

    st.write(f"### Data untuk Musim {season_option} dan Rentang Tanggal {date_range[0]} - {date_range[1]}")
    st.write(filtered_data.head())

    # Pilihan jenis visualisasi
    st.sidebar.subheader("Pilih Visualisasi")
    plot_type = st.sidebar.selectbox("Pilih jenis grafik:", ["Boxplot", "Scatterplot", "Histogram"])

    st.subheader("Visualisasi Data")

    if plot_type == "Boxplot":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(x='weathersit', y='cnt', data=filtered_data, ax=ax)
        ax.set_title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
        ax.set_xlabel('Kondisi Cuaca')
        ax.set_ylabel('Jumlah Penyewaan Sepeda')
        st.pyplot(fig)

    elif plot_type == "Scatterplot":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x='temp', y='cnt', data=filtered_data, alpha=0.5, ax=ax)
        ax.set_title('Hubungan Suhu dengan Jumlah Penyewaan Sepeda')
        ax.set_xlabel('Suhu')
        ax.set_ylabel('Jumlah Penyewaan Sepeda')
        st.pyplot(fig)

    elif plot_type == "Histogram":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(filtered_data["hum"], bins=30, kde=True, color="purple", ax=ax)
        ax.set_title("Distribusi Kelembapan Udara")
        ax.set_xlabel("Kelembapan")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)

else:
    st.warning("Tidak ada data untuk ditampilkan.")
