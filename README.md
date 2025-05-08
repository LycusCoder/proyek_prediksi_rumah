# 📊 Prediksi Harga Rumah di Indonesia 🇮🇩

**Oleh: Nourivex**

Proyek ini adalah script sederhana berbasis Python untuk memprediksi harga rumah di Indonesia menggunakan **Linear Regression**. Diharapkan bisa menjadi inspirasi dan referensi bagi siapa pun yang ingin belajar data science dengan konteks lokal.

---

## 🚀 Fitur Utama

* 🧹 **Pra-pemrosesan data otomatis**: termasuk normalisasi harga dan encoding lokasi
* 🏠 **Prediksi harga rumah** menggunakan regresi linier
* 📈 **Visualisasi hasil**: perbandingan aktual vs prediksi dan analisis residual
* 📁 Dukungan untuk dataset `.csv` lokal

---

## 🛠️ Teknologi dan Library

* Python 3.x
* [pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)
* [scikit-learn](https://scikit-learn.org/)
* [matplotlib](https://matplotlib.org/)
* [seaborn](https://seaborn.pydata.org/)

---

## 📂 Struktur Folder

```
.
├── data/
│   └── rumah_indonesia.csv      ← Dataset berisi informasi rumah
├── visualizations/
│   ├── aktual_vs_prediksi.png   ← Visualisasi perbandingan nilai aktual dan prediksi
│   └── residual_plot.png        ← Visualisasi residual error model
├── prediksi_rumah.py            ← Skrip utama untuk melakukan prediksi harga rumah
├── requirements.txt             ← Daftar library Python yang dibutuhkan
└── README.md                    ← Berkas penjelasan umum proyek
```

---

## 📉 Cara Kerja Singkat

1. Dataset dimuat dan dibersihkan (hilangkan missing value, ubah harga ke format integer).
2. Kolom lokasi dikonversi menjadi numerik via one-hot encoding.
3. Dataset dipisah jadi data latih dan uji.
4. Model Linear Regression dilatih dan diuji.
5. Hasil evaluasi (RMSE & R²) ditampilkan.
6. Grafik hasil disimpan ke folder `visualizations/`.

---

## 💡 Contoh Output

```bash
RMSE: 362000000.00 | R²: 0.8452
Visualisasi disimpan di folder 'visualizations/'.
```

---

## 📌 Catatan

* Pastikan folder `data/` dan `visualizations/` sudah ada.
* File dataset harus bernama `rumah_indonesia.csv` dan memiliki kolom seperti:
  `luas_meter2, kamar_tidur, kamar_mandi, jarak_ke_kota (km), tahun_bangun, lokasi, harga (Rp)`.

---

## ❤️ Penutup

Proyek ini dibuat sebagai latihan pribadi dan semoga bisa berguna untuk siapa pun yang ingin memahami dasar-dasar prediksi harga rumah dengan data Indonesia.

Kalau kamu terbantu atau tertarik untuk mengembangkan lebih jauh, jangan ragu untuk forking dan kontribusi!

