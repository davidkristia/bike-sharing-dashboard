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

        # Cek apakah kedua kolom weekday_x dan weekday_y ada
        if "weekday_x" in df.columns and "weekday_y" in df.columns:
            # Jika isinya sama, gunakan salah satu dan hapus yang lain
            if df["weekday_x"].equals(df["weekday_y"]):
                df.rename(columns={"weekday_x": "weekday"}, inplace=True)
                df.drop(columns=["weekday_y"], inplace=True)
            else:
                df.rename(columns={"weekday_x": "weekday"}, inplace=True)
        
        elif "weekday_x" in df.columns:
            df.rename(columns={"weekday_x": "weekday"}, inplace=True)
        
        elif "weekday_y" in df.columns:
            df.rename(columns={"weekday_y": "weekday"}, inplace=True)

        # Konversi tanggal
        df["dteday"] = pd.to_datetime(df["dteday"])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None:
    st.sidebar.subheader("Filter Data")
    
    # Filter berdasarkan musim
    season_option = st.sidebar.selectbox("Pilih Musim:", sorted(df["season"].unique()))
    
    # Filter berdasarkan rentang tanggal
    min_date = df["dteday"].min().date()
    max_date = df["dteday"].max().date()
    date_range = st.sidebar.date_input("Pilih Rentang Tanggal:", [min_date, max_date], min_value=min_date, max_value=max_date)
    
    # Filter berdasarkan rentang suhu
    temp_range = st.sidebar.slider("Pilih Rentang Suhu:", float(df["temp"].min()), float(df["temp"].max()), (float(df["temp"].min()), float(df["temp"].max())))

    # Filter berdasarkan hari dalam seminggu
    day_option = st.sidebar.multiselect("Pilih Hari dalam Seminggu:", options=sorted(df["weekday"].unique()), default=sorted(df["weekday"].unique()))

    # Terapkan filter
    filtered_data = df[
        (df["season"] == season_option) & 
        (df["dteday"].between(pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1]))) & 
        (df["temp"].between(temp_range[0], temp_range[1])) &
        (df["weekday"].isin(day_option))
    ]
    
    st.subheader("Data Penyewaan Sepeda yang Difilter")
    st.write(filtered_data.head())
    
    # Pilihan jenis visualisasi
    st.sidebar.subheader("Pilih Visualisasi")
    plot_type = st.sidebar.selectbox("Pilih jenis grafik:", ["Boxplot", "Scatterplot", "Histogram", "Heatmap Pola Waktu"]) 

    st.subheader("Visualisasi Data")
    
    if plot_type == "Boxplot":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.boxplot(x='weathersit', y='cnt', data=filtered_data, ax=ax)
        ax.set_title('Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda')
        ax.set_xlabel('Kondisi Cuaca')
        ax.set_ylabel('Jumlah Penyewaan Sepeda')
        st.pyplot(fig)
    
    elif plot_type == "Scatterplot":
        scatter_option = st.radio("Pilih Variabel Independent:", ("Suhu", "Kelembapan"))
        fig, ax = plt.subplots(figsize=(10, 5))
        
        if scatter_option == "Suhu":
            sns.scatterplot(x='temp', y='cnt', data=filtered_data, alpha=0.5, ax=ax)
            ax.set_title("Hubungan Suhu dengan Jumlah Penyewaan Sepeda")
            ax.set_xlabel("Suhu")
        else:
            sns.scatterplot(x='hum', y='cnt', data=filtered_data, color="blue", alpha=0.5, ax=ax)
            ax.set_title("Hubungan Kelembapan Udara dengan Jumlah Peminjaman Sepeda")
            ax.set_xlabel("Kelembapan Udara")
        
        ax.set_ylabel('Jumlah Peminjaman Sepeda')
        st.pyplot(fig)
    
    elif plot_type == "Histogram":
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.histplot(filtered_data["hum"], bins=30, kde=True, color="purple", ax=ax)
        ax.set_title("Distribusi Kelembapan Udara")
        ax.set_xlabel("Kelembapan")
        ax.set_ylabel("Frekuensi")
        st.pyplot(fig)
    
    elif plot_type == "Heatmap Pola Waktu":
        st.subheader("Heatmap Penyewaan Sepeda per Jam dan Hari")
        pivot_table = filtered_data.pivot_table(index='weekday', columns='hr', values='cnt', aggfunc='mean')
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.heatmap(pivot_table, cmap="coolwarm", linewidths=0.5, ax=ax)
        ax.set_title("Heatmap Penyewaan Sepeda per Jam dan Hari")
        ax.set_xlabel("Jam")
        ax.set_ylabel("Hari dalam Seminggu")
        st.pyplot(fig)

else:
    st.warning("Data tidak dapat dimuat. Periksa kembali file CSV yang digunakan.")
