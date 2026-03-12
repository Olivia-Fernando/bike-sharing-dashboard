\# Bike Sharing Dashboard



\## Deskripsi Project

Project ini bertujuan untuk menganalisis pola penyewaan sepeda menggunakan \*\*Bike Sharing Dataset\*\*.  

Analisis dilakukan untuk mengetahui pengaruh faktor seperti \*\*musim, suhu, dan hari kerja\*\* terhadap jumlah penyewaan sepeda.



Dari analisis, ditemukan bahwa:  

\- Penyewaan sepeda paling tinggi pada musim \*\*Summer\*\* dan \*\*Fall\*\*.  

\- Jumlah penyewaan cenderung meningkat seiring dengan kenaikan \*\*suhu\*\*.  

\- Hari kerja dan akhir pekan memiliki pola penyewaan yang berbeda.



Dashboard ini dibuat menggunakan \*\*Streamlit\*\*, sehingga dapat diakses secara interaktif.



---



\## Struktur Folder



```text

submission/

├── dashboard/

│   ├── dashboard.py

│   └── main\_data.csv

├── data/

│   ├── day.csv

│   ├── hour.csv

│   └── Readme.txt

├── notebook.ipynb

├── README.md

├── requirements.txt

└── url.txt

---

\## Menjalankan Dashboard



1\. Pastikan berada di folder `submission/`



2\. Install library yang dibutuhkan:



```bash

pip install -r requirements.txt





\## Jalankan dashboard:



streamlit run dashboard/dashboard.py



Browser akan terbuka secara otomatis menampilkan dashboard interaktif.



\## Dashboard Live



\## Dashboard dapat diakses secara live di:

https://bike-sharing-dashboard-hch9qjhkzicyag6zpqvm4f.streamlit.app/](https://bike-sharing-dashboard-fxsuz8nykzgntbgotext4d.streamlit.app/





\## Insight Analisis Data



* Musim Summer dan Fall memiliki total penyewaan sepeda tertinggi.



* Jumlah penyewaan sepeda meningkat seiring dengan kenaikan suhu.



* Perbedaan hari kerja dan akhir pekan memengaruhi pola penyewaan sepeda.





