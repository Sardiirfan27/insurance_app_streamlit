
# 🚀 Machine Learning App dengan Streamlit

Project ini dibuat sebagai materi pembelajaran untuk membuat aplikasi sederhana menggunakan streamlit.

Aplikasi ini dibuat menggunakan **Python** dan beberapa pustaka lainnya seperti **Streamlit, Scikit-learn, matplotlib, seaborn, dll**. 

Model Machine Learning disimpan dalam format `.joblib` dan dipanggil di aplikasi untuk melakukan inferensi berdasarkan input pengguna.

---

## 📂 Struktur Project
```

insurance_app/
├── data/
│   ├── insurance.csv
│   └── inference.csv
├── notebooks/
│   └── insurance.ipynb
├── models/
│   └── insurance_model.joblib
├── app.py
└── pages/
    ├── 1_visualization.py
    └── 2_prediction.py

````

---

## ⚙️ Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Buat virtual environment (opsional tapi disarankan)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```
---

## ▶️ Menjalankan Aplikasi

Jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

Aplikasi akan berjalan di browser pada alamat:

```
http://localhost:8501
```

---

## 🛠️ Fitur

* ✅ Memuat model Machine Learning dari file `.joblib`
* ✅ Prediksi berdasarkan input pengguna
* ✅ Antarmuka web interaktif menggunakan **Streamlit**
* ✅ Mudah di-deploy ke **Streamlit Cloud** atau **Heroku**

---

## 📌 Catatan

* Anda dapat menggunakan file `inference.csv` untuk melakukan pada menu prediksi dari file csv. 
* File `.gitignore` sudah ditambahkan agar file tidak penting (seperti `__pycache__` atau `venv/`) tidak ikut masuk ke repository.
* Jika file model sangat besar (>50MB), disarankan untuk menyimpannya di layanan penyimpanan cloud (misalnya Google Drive atau Hugging Face Hub) dan memuatnya secara dinamis.

---

## 📄 Lisensi

Proyek ini menggunakan lisensi **MIT** – bebas digunakan, dimodifikasi, dan dibagikan.

```
