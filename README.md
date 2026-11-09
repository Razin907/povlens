# PovertyLens — Household Poverty Level Prediction & Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**PovertyLens** adalah aplikasi berbasis **Machine Learning** dan dashboard interaktif **Streamlit** untuk memprediksi dan menganalisis tingkat kerentanan kemiskinan rumah tangga (*Household Poverty Level*) berdasarkan indikator sosioekonomi, demografi, dan kondisi tempat tinggal.

Dataset proyek ini mengacu pada kompetisi [Costa Rican Household Poverty Level Prediction](https://www.kaggle.com/c/costa-rican-household-poverty-prediction) oleh **Inter-American Development Bank (IDB)**.

## Problem Background & Objective

Banyak program bantuan sosial menghadapi tantangan dalam mengidentifikasi keluarga yang paling membutuhkan bantuan secara akurat (*proxy means test*). Proyek ini bertujuan untuk:

1. Membangun model klasifikasi multi-kelas untuk memprediksi tingkat kemiskinan rumah tangga secara objektif.
2. Memberikan antarmuka interaktif bagi pengambil kebijakan atau pengguna umum untuk menguji data baru baik secara manual maupun *batch upload* (CSV).
3. Memvisualisasikan distribusi dan probabilitas tingkat kemiskinan agar keputusan intervensi sosial lebih transparan.

## Target Klasifikasi

| Level | Kategori | Keterangan |
| :---: | :--- | :--- |
| **1** | Kemiskinan Ekstrem (*Extreme Poverty*) | Rumah tangga dengan prioritas bantuan tertinggi |
| **2** | Kemiskinan Moderat (*Moderate Poverty*) | Rumah tangga miskin dengan kebutuhan bantuan dasar |
| **3** | Rumah Tangga Rentan (*Vulnerable Household*) | Berisiko tinggi jatuh ke jurang kemiskinan |
| **4** | Rumah Tangga Tidak Rentan (*Non-Vulnerable*) | Rumah tangga dengan kondisi ekonomi relatif stabil |

## Fitur Utama Dashboard

- **Data Overview:** Eksplorasi ringkasan data, distribusi kelas target, serta rata-rata variabel penting (tingkat pendidikan, kepadatan hunian, dll.).
- **Manual Feature Input:** Input interaktif menggunakan slider dan selectbox untuk mensimulasikan karakteristik rumah tangga.
- **Batch CSV Upload:** Dukungan upload file CSV untuk melakukan inferensi banyak data sekaligus.
- **Probability Distribution:** Visualisasi diagram batang probabilitas untuk setiap kelas target dari model Machine Learning.

## Variabel / Fitur yang Digunakan

Model menggunakan 12 fitur sosioekonomi utama yang telah diseleksi:

1. `meaneduc` — Rata-rata lama sekolah orang dewasa (tahun)
2. `escolari` — Lama sekolah yang telah diselesaikan
3. `edjefe` — Lama sekolah kepala keluarga
4. `hogar_nin` — Jumlah anak dalam rumah tangga (0–19 tahun)
5. `rooms` — Jumlah ruangan dalam rumah
6. `overcrowding` — Rasio kepadatan (orang per kamar)
7. `v18q` — Kepemilikan tablet (Ya / Tidak)
8. `pisomoscer` — Lantai keramik / mosaik (Ya / Tidak)
9. `cielorazo` — Memiliki plafon / langit-langit (Ya / Tidak)
10. `epared3` — Dinding dalam kondisi baik (Ya / Tidak)
11. `etecho3` — Atap dalam kondisi baik (Ya / Tidak)
12. `eviv3` — Kondisi rumah secara umum baik (Ya / Tidak)


## Cara Menjalankan Proyek Secara Lokal

### 1. Clone Repositori

```bash
git clone https://github.com/USERNAME/povlens.git
cd povlens
```

### 2. Buat & Aktifkan Virtual Environment (Opsional)

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

Aplikasi akan otomatis terbuka di browser pada alamat `http://localhost:8501`.

---

## Struktur Repositori

```text
├── app.py                         # Aplikasi web Streamlit
├── generate_poverty_level.pkl     # Model ML terlatih + Scaler + Metadata
├── data.csv                       # Dataset bersih
├── contoh_input.csv               # Contoh file CSV untuk pengujian batch upload
├── P8 - Project Capstone I.ipynb  # Notebook EDA & Data Cleaning
├── P8 - Project Capstone II.ipynb # Notebook Training, Tuning, & Evaluasi Model
├── P8 - Project Capstone III.ipynb# Notebook Deployment & Persiapan Streamlit
├── requirements.txt               # Daftar pustaka Python
└── README.md                      # Dokumentasi proyek
```

---

## Kontributor & Peran

- **Razin Hafid Hamdi** — *Data Cleaning, Exploratory Data Analysis (EDA) & Feature Engineering*

- **Lutfia Laila Ramadhani** — *Model Training, Hyperparameter Tuning & Cross Validation*

- **Mia Almusdari** — *Streamlit Web Dashboard Development, Model Serialization & Documentation*

---

## Lisensi

Didistribusikan di bawah lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.
