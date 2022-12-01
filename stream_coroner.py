import pickle
import streamlit as st

# membaca model
coroner_model = pickle.load(open('coroner_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi Jantung Koroner')

sbp = st.text_input('Masukan Tekanan Darah Sistolik')

tobacco = st.text_input('Penggunaan tembakau tahunan (dalam kg)')

ldl = st.text_input('Masukan lipoprotein densitas rendah (Idl)')

adiposity = st.text_input('Tingkat adipositas (adiposty)')

typea = st.text_input('Masukan skor kepribadian tipe A (typea)')

obesity = st.text_input('Tingkat obesitas (indeks massa tubuh)')

alcohol = st.text_input('Tingkat penggunaan alkohol')

age = st.text_input('Masukan Usia')

# code untuk kelompok jenis
coroner_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    ane_prediction = coroner_model.predict([[sbp, tobacco, ldl, adiposity, typea, obesity, alcohol, age]])
    
    if(ane_prediction[0] == 1):
        coroner_diagnosis = 'Pasien mengidap Jantung Koroner'
    else :
        coroner_diagnosis = 'Pasien tidak mengidap Jantung Koroner'

    st.success(coroner_diagnosis)
