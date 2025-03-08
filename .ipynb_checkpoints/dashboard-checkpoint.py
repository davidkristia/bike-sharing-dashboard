import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data_path = r'C:\Users\DAVID\DBS\dashboard\main_data.csv'
df = pd.read_csv(data_path)

# Konfigurasi halaman
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Judul Dashboard
st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis penyewaan sepeda berdasarkan cuaca dan waktu.")

# Sidebar untuk filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim", df['season'].unique())
filtered_df = df[df['season'] == selected_season]

# Visualisasi jumlah penyewaan sepeda berdasarkan cuaca
st.subheader("📊 Pengaruh Cuaca terhadap Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(x='weathersit', y='cnt', data=filtered_df, ax=ax)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# Visualisasi tren penyewaan sepeda harian
st.subheader("📈 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='dteday', y='cnt', data=filtered_df, ax=ax)
plt.xticks(rotation=45)
plt.xlabel("Tanggal")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Visualisasi pola penggunaan sepeda berdasarkan jam
st.subheader("⏳ Pola Penyewaan Sepeda Berdasarkan Jam")
if 'hr' in df.columns:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x='hr', y='cnt', data=df, ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
else:
    st.write("Data jam tidak tersedia dalam main_data.csv.")

st.write("📌 **Kesimpulan:**")
st.write("- Cuaca mempengaruhi jumlah penyewaan sepeda secara signifikan.")
st.write("- Tren penyewaan sepeda bervariasi berdasarkan musim dan waktu.")

st.write("✅ **Dashboard dibuat dengan Streamlit.**")
