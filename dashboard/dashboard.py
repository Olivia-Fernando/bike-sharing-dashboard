import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Bike Sharing Data Dashboard")

# Load dataset
data = pd.read_csv("../data/day.csv")

st.subheader("Preview Dataset")
st.write(data.head())

# Visualisasi berdasarkan season
st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")

season_rentals = data.groupby("season")["cnt"].sum()

fig, ax = plt.subplots()
season_rentals.plot(kind="bar", ax=ax)

plt.xlabel("Season")
plt.ylabel("Total Rentals")

st.pyplot(fig)

# Visualisasi suhu
st.subheader("Pengaruh Suhu terhadap Penyewaan Sepeda")

fig2, ax2 = plt.subplots()
ax2.scatter(data["temp"], data["cnt"])

ax2.set_xlabel("Temperature")
ax2.set_ylabel("Total Rentals")

st.pyplot(fig2)