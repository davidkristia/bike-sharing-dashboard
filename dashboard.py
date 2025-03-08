import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load dataset dengan path relatif
data_path = os.path.join(os.path.dirname(__file__), "main_data.csv")

# Streamlit App Title
st.title("Dashboard Bike Sharing Dataset")

# Sidebar - Pilihan Dataset
dataset_option = st.sidebar.selectbox("Pilih Dataset:", ["Day Data", "Hour Data"])

# Menampilkan Data
if dataset_option == "Day Data":
    st.write("## Day Dataset")
    st.write(day_df.head())
else:
    st.write("## Hour Dataset")
    st.write(hour_df.head())

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(day_df.describe() if dataset_option == "Day Data" else hour_df.describe())

# Visualisasi Distribusi Penyewaan Sepeda berdasarkan Cuaca
st.subheader("Distribusi Penyewaan Sepeda berdasarkan Cuaca")
fig, ax = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=day_df if dataset_option == "Day Data" else hour_df, ax=ax)
st.pyplot(fig)

# Filter Data berdasarkan Musim
st.sidebar.subheader("Filter Data")
season_option = st.sidebar.selectbox("Pilih Musim:", [1, 2, 3, 4])
filtered_data = day_df[day_df['season'] == season_option] if dataset_option == "Day Data" else hour_df[hour_df['season'] == season_option]
st.write(f"### Data untuk Musim {season_option}")
st.write(filtered_data.head())
