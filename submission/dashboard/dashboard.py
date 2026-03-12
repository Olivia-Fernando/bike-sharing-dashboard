import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# Judul Dashboard
# ==============================
st.title("Bike Sharing Data Dashboard")

st.write("""
Dashboard ini menampilkan analisis sederhana dari **Bike Sharing Dataset**
untuk melihat pola penyewaan sepeda berdasarkan musim dan suhu.
""")

# ==============================
# Load dataset dengan path aman
# ==============================
BASE_DIR = os.path.dirname(__file__)  # folder tempat dashboard.py berada
data_path = os.path.join(BASE_DIR, "main_data.csv")

try:
    data = pd.read_csv(data_path)
    st.success("Dataset berhasil dimuat!")
except FileNotFoundError:
    st.error(f"File CSV tidak ditemukan di path: {data_path}")
    st.stop()  # hentikan eksekusi jika CSV tidak ada

# ==============================
# Preview Dataset
# ==============================
st.subheader("Preview Dataset")
st.dataframe(data.head())

# ==============================
# Debug / Cek Kolom
# ==============================
st.write("Kolom dataset:", data.columns.tolist())

# ==============================
# Mapping season (auto-detect tipe data)
# ==============================
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}

if data["season"].dtype in ["int64", "float64"]:
    # Jika season angka, lakukan mapping
    data["season"] = data["season"].astype(int).map(season_map)
else:
    # Jika season sudah teks, gunakan langsung
    data["season"] = data["season"]

st.write("Season setelah normalisasi:", data["season"].unique())

# ==============================
# Visualisasi 1: Total Penyewaan Sepeda per Musim
# ==============================
st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")
season_rentals = data.groupby("season")["cnt"].sum()

if season_rentals.empty:
    st.warning("Data season kosong, tidak bisa menampilkan grafik.")
else:
    fig, ax = plt.subplots()
    season_rentals.plot(kind="bar", ax=ax)
    ax.set_xlabel("Season")
    ax.set_ylabel("Total Rentals")
    ax.set_title("Bike Rentals per Season")
    st.pyplot(fig)

# ==============================
# Visualisasi 2: Pengaruh Suhu terhadap Penyewaan Sepeda
# ==============================
st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")

# Pastikan kolom temp dan cnt ada
if "temp" not in data.columns or "cnt" not in data.columns:
    st.warning("Kolom 'temp' atau 'cnt' tidak ada, grafik suhu tidak bisa ditampilkan.")
else:
    fig2, ax2 = plt.subplots()
    ax2.scatter(data["temp"], data["cnt"])
    ax2.set_xlabel("Temperature")
    ax2.set_ylabel("Total Rentals")
    ax2.set_title("Temperature vs Bike Rentals")
    st.pyplot(fig2)

# ==============================
# Insight
# ==============================
st.subheader("Insight")
st.write("""
- Penyewaan sepeda lebih tinggi pada musim tertentu seperti summer dan fall.
- Suhu memiliki hubungan positif terhadap jumlah penyewaan sepeda.
- Ketika suhu meningkat, jumlah penyewaan sepeda juga cenderung meningkat.
""")