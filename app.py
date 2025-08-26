import streamlit as st

def main():
    st.set_page_config(
        page_title="Insurance Prediction App",
        page_icon="💡",
        layout="wide"
    )

    # Judul utama
    st.title("💡 Insurance Prediction App")

    # Deskripsi aplikasi
    st.markdown("""
    Selamat datang di **Insurance Prediction App** 🎉  

    Aplikasi ini dibuat untuk menganalisis dan memprediksi **biaya asuransi kesehatan** berdasarkan dataset **insurance.csv**.  
    Model machine learning telah dilatih sebelumnya dan disimpan dalam file `insurance_model.joblib`.

    ---
    """)

    # Penjelasan menu
    st.header("📑 Menu Aplikasi")
    st.markdown("""
    Aplikasi ini memiliki beberapa halaman yang dapat diakses melalui sidebar:

    1. **📊 Visualization**  
       Menampilkan berbagai visualisasi dari dataset **insurance.csv** seperti distribusi usia, BMI, perbedaan antara perokok dan bukan perokok, serta pola biaya asuransi berdasarkan fitur.

    2. **⚙️ Prediction**  
       Terdiri dari dua cara untuk melakukan prediksi:
       - **Upload CSV** → Anda dapat mengunggah file CSV dengan struktur yang sama seperti dataset asli untuk memprediksi biaya asuransi secara batch.  
       - **Input Data Manual** → Masukkan data individu (usia, jenis kelamin, BMI, jumlah anak, status perokok, dan region) untuk mendapatkan prediksi biaya asuransi.
    """)

    # Dataset
    st.header("📂 Dataset")
    st.markdown("""
    Dataset yang digunakan adalah **insurance.csv**, dengan kolom-kolom berikut:
    - `age` → Usia tertanggung  
    - `sex` → Jenis kelamin (`male` / `female`)  
    - `bmi` → Body Mass Index  
    - `children` → Jumlah anak yang ditanggung asuransi  
    - `smoker` → Status perokok (`yes` / `no`)  
    - `region` → Lokasi tempat tinggal (`northeast`, `northwest`, `southeast`, `southwest`)  
    - `charges` → Biaya asuransi (target/predictand)

    Kolom `charges` hanya ada pada dataset latih, dan tidak perlu disertakan saat melakukan prediksi.
    """)

    # Footer
    st.markdown("---")
    st.info("👨‍💻 Dibuat untuk pembelajaran Machine Learning dan Deployment dengan Streamlit.")

if __name__ == "__main__":
    main()
