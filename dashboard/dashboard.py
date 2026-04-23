import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚴", layout="wide")

st.title("🚴 Bike Sharing Data Dashboard")
st.write("Dashboard analisis interaktif **Bike Sharing Dataset** — pola penyewaan berdasarkan musim, suhu, dan jenis hari.")

# ── Load data ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "main_data.csv")

try:
    data = pd.read_csv(data_path)
except FileNotFoundError:
    st.error(f"File CSV tidak ditemukan: {data_path}")
    st.stop()

# ── Normalisasi ──
data["dteday"] = pd.to_datetime(data["dteday"])

# Season: pastikan selalu jadi string nama musim
season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
if data["season"].dtype in ["int64", "float64"]:
    data["season"] = data["season"].astype(int).map(season_map)

# Workingday: pastikan selalu jadi string
wd_map = {0: "Weekend/Holiday", 1: "Working Day"}
if data["workingday"].dtype in ["int64", "float64"]:
    data["workingday"] = data["workingday"].astype(int).map(wd_map)

# ── Sidebar Filter ──
st.sidebar.header("🔧 Filter Data")

# Filter musim
season_options = ["Spring", "Summer", "Fall", "Winter"]
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim:",
    options=season_options,
    default=season_options
)

# Filter jenis hari
wd_options = ["Working Day", "Weekend/Holiday"]
selected_wd = st.sidebar.multiselect(
    "Pilih Jenis Hari:",
    options=wd_options,
    default=wd_options
)

# Filter rentang tahun
st.sidebar.markdown("**Pilih Rentang Tahun:**")
col_s, col_e = st.sidebar.columns(2)
min_year = int(data["dteday"].dt.year.min())
max_year = int(data["dteday"].dt.year.max())
start_year = col_s.number_input("Dari", min_value=2000, max_value=2100, value=min_year, step=1)
end_year = col_e.number_input("Sampai", min_value=2000, max_value=2100, value=max_year, step=1)

# ── Terapkan Filter ──
filtered = data.copy()

if selected_seasons:
    filtered = filtered[filtered["season"].isin(selected_seasons)]

if selected_wd:
    filtered = filtered[filtered["workingday"].isin(selected_wd)]

filtered = filtered[
    (filtered["dteday"].dt.year >= start_year) &
    (filtered["dteday"].dt.year <= end_year)
]

# ── Metrik Ringkasan ──
st.subheader("📊 Ringkasan Data")
c1, c2, c3 = st.columns(3)
c1.metric("Total Penyewaan", f"{filtered['cnt'].sum():,.0f}")
c2.metric("Rata-rata Harian", f"{filtered['cnt'].mean():,.0f}" if not filtered.empty else "0")
c3.metric("Jumlah Data", f"{len(filtered):,} hari")
st.markdown("---")

# ── Visualisasi 1: Per Musim ──
st.subheader("🍂 Total Penyewaan per Musim")

if filtered.empty:
    st.warning("Tidak ada data untuk filter yang dipilih.")
else:
    season_rentals = filtered.groupby("season")["cnt"].sum().reindex(
        [s for s in ["Fall","Summer","Winter","Spring"] if s in filtered["season"].unique()]
    ).dropna()

    colors = ["#FF6B35" if v == season_rentals.max() else "#72BCD4" for v in season_rentals.values]
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    bars = ax1.bar(season_rentals.index, season_rentals.values, color=colors)
    for bar in bars:
        h = bar.get_height()
        ax1.annotate(f"{h:,.0f}", xy=(bar.get_x()+bar.get_width()/2, h),
                     xytext=(0,3), textcoords="offset points", ha="center", va="bottom", fontsize=10)
    ax1.set_xlabel("Musim", fontsize=12)
    ax1.set_ylabel("Total Penyewaan", fontsize=12)
    ax1.set_title("Total Penyewaan Sepeda per Musim", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig1)
    st.info(f"🏆 Tertinggi: **{season_rentals.idxmax()}** — {season_rentals.max():,.0f} penyewaan")

st.markdown("---")

# ── Visualisasi 2: Suhu ──
st.subheader("🌡️ Pengaruh Suhu terhadap Penyewaan")

if not filtered.empty:
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sc = ax2.scatter(filtered["temp"], filtered["cnt"], alpha=0.5,
                     c=filtered["cnt"], cmap="YlOrRd", edgecolors="none")
    plt.colorbar(sc, ax=ax2, label="Jumlah Penyewaan")
    ax2.set_xlabel("Suhu (Normalized)", fontsize=12)
    ax2.set_ylabel("Total Penyewaan", fontsize=12)
    ax2.set_title("Hubungan Suhu dengan Jumlah Penyewaan Sepeda", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig2)
    corr = filtered["temp"].corr(filtered["cnt"])
    st.info(f"📈 Korelasi suhu vs penyewaan: **{corr:.2f}**")

st.markdown("---")

# ── Visualisasi 3: Hari Kerja vs Weekend ──
st.subheader("📅 Hari Kerja vs Weekend/Holiday")

if not filtered.empty and "workingday" in filtered.columns:
    wd_avg = filtered.groupby("workingday")["cnt"].mean()
    fig3, ax3 = plt.subplots(figsize=(6, 5))
    bar_colors = ["#2A9D8F" if k == "Working Day" else "#F4A261" for k in wd_avg.index]
    wd_avg.plot(kind="bar", ax=ax3, color=bar_colors, rot=0)
    for bar in ax3.patches:
        ax3.annotate(f"{bar.get_height():,.0f}",
                     xy=(bar.get_x()+bar.get_width()/2, bar.get_height()),
                     xytext=(0,3), textcoords="offset points", ha="center", va="bottom", fontsize=10)
    ax3.set_xlabel("Jenis Hari", fontsize=12)
    ax3.set_ylabel("Rata-rata Penyewaan", fontsize=12)
    ax3.set_title("Rata-rata Penyewaan: Hari Kerja vs Weekend", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig3)

st.markdown("---")

# ── Insight ──
st.subheader("💡 Insight")
st.write("""
- **Musim Fall** memiliki total penyewaan tertinggi (32,2% dari keseluruhan), rata-rata 5.644 penyewaan/hari.
- **Musim Spring** memiliki penyewaan terendah (14,3%), rata-rata hanya 2.604 penyewaan/hari.
- **Suhu** berkorelasi positif cukup kuat (r = 0.627) dengan jumlah penyewaan.
- Rata-rata penyewaan **hari kerja** (4.585/hari) sedikit lebih tinggi dari **weekend** (4.330/hari).
""")
