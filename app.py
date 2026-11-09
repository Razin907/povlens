import streamlit as st
import pandas as pd
import pickle
import time
import os

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Prediksi Kemiskinan", layout="wide")

st.write("""
# Selamat Datang di Dashboard Pemodelan Machine Learning

Dibuat oleh: **Kelompok 2**
""")

# Pilihan menu navigasi di sidebar
add_selectitem = st.sidebar.selectbox("Pilih Menu:", ("Level Kemiskinan", "Gambaran Umum Data"))

MODEL_FILE = "generate_poverty_level.pkl"


@st.cache_resource
def load_bundle():
    with open(MODEL_FILE, 'rb') as file:
        return pickle.load(file)


def poverty():
    st.write("""
    Dashboard ini memprediksi **tingkat kemiskinan rumah tangga** (*Household Poverty Level*) di Kosta Rika.

    Dataset bersumber dari kompetisi [Costa Rican Household Poverty Level Prediction](https://www.kaggle.com/c/costa-rican-household-poverty-prediction) oleh Inter-American Development Bank (IDB).

    | Level | Kategori | Keterangan |
    | :---: | :--- | :--- |
    | **1** | Kemiskinan Ekstrem | Rumah tangga dengan kebutuhan bantuan paling mendesak |
    | **2** | Kemiskinan Moderat | Rumah tangga yang berada di bawah garis kemiskinan |
    | **3** | Rumah Tangga Rentan | Berisiko tinggi jatuh ke kategori miskin |
    | **4** | Tidak Rentan | Kondisi ekonomi rumah tangga relatif aman dan stabil |
    """)

    if not os.path.exists(MODEL_FILE):
        st.error(f"File model '{MODEL_FILE}' belum ditemukan. Pastikan kamu sudah menjalankan Capstone II hingga selesai dan menyimpan file model di folder yang sama.")
        return

    bundle = load_bundle()
    features = bundle['features']
    info = bundle['feature_info']
    labels = bundle['target_labels']

    st.sidebar.header('Input Data Rumah Tangga:')
    
    # Opsi unggah file CSV
    uploaded_file = st.sidebar.file_uploader(
        "Unggah file CSV", 
        type=["csv"],
        help="Pastikan file CSV memuat 12 kolom fitur yang sesuai."
    )

    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        missing_cols = [c for c in features if c not in input_df.columns]
        if missing_cols:
            st.error(f"Kolom berikut belum ditemukan di file CSV kamu: {missing_cols}")
            return
        input_df = input_df[features]
    else:
        def user_input_features():
            st.sidebar.subheader('Input Manual:')
            values = {}
            for col in features:
                meta = info[col]
                if meta['type'] == 'binary':
                    pilihan = st.sidebar.selectbox(meta['desc'], ('Tidak', 'Ya'),
                                                   index=int(meta['default']), key=col)
                    values[col] = 1 if pilihan == 'Ya' else 0
                elif meta['type'] == 'int':
                    values[col] = st.sidebar.slider(meta['desc'], int(meta['min']), int(meta['max']),
                                                    int(meta['default']), key=col)
                else:
                    values[col] = st.sidebar.slider(meta['desc'], float(meta['min']), float(meta['max']),
                                                    float(meta['default']), key=col)
            return pd.DataFrame(values, index=[0])

        input_df = user_input_features()

    if st.sidebar.button('Prediksi Sekarang!'):
        df = input_df
        st.write("**Data yang dimasukkan:**")
        st.dataframe(df)

        loaded_model = bundle['model']
        scaled = bundle['scaler'].transform(df[features])
        prediction = loaded_model.predict(scaled)
        proba = loaded_model.predict_proba(scaled)

        st.subheader('Hasil Prediksi:')
        with st.spinner('Sedang menganalisis data...'):
            time.sleep(1)
            for i in range(len(df)):
                level = int(prediction[i])
                st.success(f"Data baris ke-{i + 1}: **Level {level} - {labels[level]}**")

        st.write("**Peluang (probabilitas) tiap level untuk baris pertama:**")
        proba_df = pd.DataFrame({'Probabilitas': proba[0]},
                                index=[f"Level {int(c)}: {labels[int(c)]}" for c in loaded_model.classes_])
        st.bar_chart(proba_df)
        st.caption(f"Model yang digunakan: **{bundle['model_name']}**. Hasil ini merupakan estimasi berbasis 12 fitur sosioekonomi dan berfungsi sebagai bahan pertimbangan.")


def overview():
    st.write("""
    Halaman ini menampilkan gambaran umum dan ringkasan statistik dari dataset bersih (**data.csv**) hasil olahan Capstone I.
    """)
    if not os.path.exists("data.csv"):
        st.error("File 'data.csv' tidak ditemukan. Silakan jalankan Capstone I terlebih dahulu.")
        return

    data = pd.read_csv("data.csv", index_col=0)
    order = ['Ekstrem', 'Moderat', 'Rentan', 'Tidak rentan']
    counts = data['Target'].value_counts().reindex(order)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rumah Tangga", f"{len(data):,}")
    col2.metric("Jumlah Kolom / Fitur", data.shape[1])
    col3.metric("Rata-rata Lama Sekolah Dewasa", f"{data['meaneduc'].mean():.1f} tahun")

    st.subheader("Distribusi Tingkat Kemiskinan")
    st.bar_chart(counts)

    st.subheader("Rata-rata Variabel Utama per Tingkat Kemiskinan")
    ringkas = data.groupby('Target')[['meaneduc', 'overcrowding', 'hogar_nin', 'rooms']].mean().reindex(order).round(2)
    st.dataframe(ringkas)


if add_selectitem == "Level Kemiskinan":
    poverty()
elif add_selectitem == "Gambaran Umum Data":
    overview()
