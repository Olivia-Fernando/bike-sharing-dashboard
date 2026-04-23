# Bike Sharing Dashboard

## Deskripsi Project

Project ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan **Bike Sharing Dataset**.

Analisis dilakukan untuk mengetahui pengaruh faktor seperti **musim, suhu, dan hari kerja** terhadap jumlah penyewaan sepeda pada rentang tahun 2011–2012.

Dari analisis, ditemukan bahwa:
- Musim **Fall (Gugur)** memiliki rata-rata penyewaan sepeda harian tertinggi, sekitar **2x lipat** dibanding musim Spring.
- Jumlah penyewaan cenderung meningkat seiring dengan kenaikan **suhu**, dengan korelasi positif sebesar 0.63.
- Hari kerja dan akhir pekan memiliki pola penyewaan yang berbeda.

Dashboard ini dibuat menggunakan **Streamlit**, sehingga dapat diakses secara interaktif.

---

## Struktur Folder

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── data_1.csv
│   ├── data_2.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Setup Environment

### Menggunakan Conda

```bash
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```

### Menggunakan Pipenv

```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## Menjalankan Dashboard

1. Pastikan sudah mengaktifkan environment dan berada di folder `submission/`

2. Install library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

3. Jalankan dashboard:

```bash
streamlit run dashboard/dashboard.py
```

Browser akan terbuka secara otomatis menampilkan dashboard interaktif.

---

## Dashboard Live

Dashboard dapat diakses secara live di:
https://bike-sharing-dashboard-olivia-fernando.streamlit.app/

---

## Insight Analisis Data

* Musim **Fall** memiliki rata-rata penyewaan sepeda tertinggi (~5.644/hari), sekitar 2x lebih tinggi dibanding musim **Spring** (~2.604/hari).
* Jumlah penyewaan sepeda meningkat seiring dengan kenaikan suhu, dengan puncak penyewaan pada rentang suhu hangat–panas.
* Perbedaan hari kerja dan akhir pekan memengaruhi pola penyewaan sepeda.
