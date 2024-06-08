# Data Mining

## Prediksi Penyakit Ginjal Kronis

Proyek ini adalah aplikasi web untuk memprediksi Penyakit Ginjal Kronis (CKD) menggunakan dataset dari Kaggle. Aplikasi ini dibangun menggunakan Python, Streamlit, dan Decision Tree Classifier.

## Fitur

- **Pembersihan dan Pra-pemrosesan Data**: Mengatasi nilai yang hilang dan mengenkode fitur kategori.
- **Pelatihan Model**: Menggunakan Decision Tree Classifier untuk memprediksi CKD.
- **Antarmuka Web**: Memungkinkan pengguna memasukkan data medis dan menerima prediksi.
- **Visualisasi**: Menampilkan pohon keputusan dan matriks kebingungan untuk evaluasi model.

## Instalasi

1. Klon repositori:
   ```sh
   git clone https://github.com/username/ckd-prediction.git
   cd ckd-prediction
   ```

2. Buat dan aktifkan lingkungan virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate   # Untuk Windows
   source venv/bin/activate # Untuk macOS/Linux
   ```

3. Instal dependensi:
   ```sh
   pip install -r requirements.txt
   ```

## Penggunaan

1. Jalankan aplikasi:
   ```sh
   streamlit run main.py
   ```

2. Buka browser web dan navigasi ke alamat server lokal yang ditampilkan (biasanya `http://localhost:8501`).

## Struktur Proyek

- **`web_function.py`**: Berisi fungsi untuk memuat data, melatih model, dan membuat prediksi.
- **`main.py`**: Mengelola logika aplikasi utama dan navigasi halaman.
- **`home.py`**: Menampilkan halaman utama aplikasi.
- **`predict.py`**: Menangani logika prediksi dan antarmuka input pengguna.
- **`visualise.py`**: Menyediakan visualisasi untuk pohon keputusan dan matriks kebingungan.

## Dataset

Dataset yang digunakan untuk proyek ini bersumber dari Kaggle: [Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease).

## Kontribusi

Kontribusi sangat diterima! Silakan fork repositori dan buat pull request dengan perubahan Anda.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file `LICENSE` untuk detailnya.

---
