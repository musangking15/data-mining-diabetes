import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# judul web
st.title('Data Mining Prediksi Diabetes')


Pregnancies = st.text_input('input nilai Pregnancies')

Glucose = st.text_input('input nilai Glucose')

BloodPressure = st.text_input('input nilai Blood Pressure')

SkinThickness = st.text_input('input nilai Skin Thickness')

Insulin = st.text_input('input nilai Insulin')

BMI = st.text_input('input nilai BMI')

DiabetesPedigreeFunction = st.text_input(
    'input nilai Diabetes Pedigree Function')

Age = st.text_input('input nilai Age')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Pasien terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
    st.success(diab_diagnosis)
