import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul Dashboard
st.title("Bike Sharing Data Dashboard")

st.write(
"""
Dashboard ini menampilkan analisis sederhana dari **Bike Sharing Dataset**
untuk melihat pola penyewaan sepeda berdasarkan musim dan suhu.
"""
)

# Load dataset
data = pd.read_csv("main_data.csv")

# Preview Dataset
st.subheader("Preview Dataset")
st.dataframe(data.head())

# Mapping season agar lebih mudah dibaca
season_map = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}

data["season"] = data["season"].map(season_map)

# ==============================
# Visualisasi 1
# ==============================

st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")

season_rentals = data.groupby("season")["cnt"].sum()

fig, ax = plt.subplots()

season_rentals.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Season")
ax.set_ylabel("Total Rentals")
ax.set_title("Bike Rentals per Season")

st.pyplot(fig)

# ==============================
# Visualisasi 2
# ==============================

st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")

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
- Penyewaan sepeda lebih tinggi pada musim tertentu seperti **summer dan fall**.
- Suhu memiliki hubungan positif terhadap jumlah penyewaan sepeda.
- Ketika suhu meningkat, jumlah penyewaan sepeda juga cenderung meningkat.
""")