import streamlit as st
import pandas as pd
import joblib

# Load model
with open("./models/insurance_model.joblib", "rb") as file:
    model = joblib.load(file)

st.title("💡 Insurance Prediction")

# Buat tab / menu
menu = st.radio("Pilih mode prediksi:", ["Upload CSV", "Input Data Manual"])

if menu == "Upload CSV":
    st.subheader("📂 Upload file CSV untuk prediksi")
    uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        st.write("📊 Data yang diupload:")
        st.dataframe(data.head())

        try:
            predictions = model.predict(data)
            data["Predicted_Charges"] = predictions
            st.success("✅ Prediksi berhasil!")
            st.dataframe(data)

            # Download hasil prediksi
            csv = data.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="💾 Download Hasil Prediksi",
                data=csv,
                file_name="insurance_predictions.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"Terjadi error saat prediksi: {e}")

elif menu == "Input Data Manual":
    st.subheader("📝 Input Data untuk Prediksi")

    # Form input
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    sex = st.selectbox("Sex", ["male", "female"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    children = st.number_input("Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

    # Convert ke DataFrame
    input_data = pd.DataFrame(
        {
            "age": [age],
            "sex": [sex],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker],
            "region": [region],
        }
    )
    #gunakan kolom selain region dan sex 
    #input_data = input_data[["age", "bmi", "smoker","children"]]


    if st.button("🔮 Prediksi"):
        try:
            
            prediction = model.predict(input_data)[0]
            st.success(f"💰 Estimasi biaya asuransi: **${prediction:,.2f}**")
        except Exception as e:
            st.error(f"Terjadi error saat prediksi: {e}")
