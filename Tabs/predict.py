import streamlit as st
import numpy as np
from web_functions import predict

def app(df, x, y):
    st.title("Halaman Prediksi")

    col1, col2, col3 = st.columns(3)

    with col1:
        bp = st.text_input("Input Nilai Blood Pressure (bp)")
        sg = st.text_input("Input Nilai Specific Gravity (sg)")
        al = st.text_input("Input Nilai Albumin (al)")
        su = st.text_input("Input Nilai Sugar (su)")
        rbc = st.selectbox("Input Nilai Red Blood Cells (rbc)", options=df['rbc'].unique())
        pc = st.selectbox("Input Nilai Pus Cell (pc)", options=df['pc'].unique())
        pcc = st.selectbox("Input Nilai Pus Cell Clumps (pcc)", options=df['pcc'].unique())
        ba = st.selectbox("Input Nilai Bacteria (ba)", options=df['ba'].unique())
    with col2:
        bgr = st.text_input("Input Nilai Blood Glucose Random (bgr)")
        bu = st.text_input("Input Nilai Blood Urea (bu)")
        sc = st.text_input("Input Nilai Serum Creatinine (sc)")
        sod = st.text_input("Input Nilai Sodium (sod)")
        pot = st.text_input("Input Nilai Potassium (pot)")
        hemo = st.text_input("Input Nilai Hemoglobin (hemo)")
        pcv = st.text_input("Input Nilai Packed Cell Volume (pcv)")
        wc = st.text_input("Input Nilai White Count (wc)")
    with col3:
        rc = st.text_input("Input Nilai Red Blood Cell Count (rc)")
        htn = st.selectbox("Input Nilai Hypertension (htn)", options=df['htn'].unique())
        dm = st.selectbox("Input Nilai Diabetes Mellitus (dm)", options=df['dm'].unique())
        cad = st.selectbox("Input Nilai Coronary Artery Disease (cad)", options=df['cad'].unique())
        appet = st.selectbox("Input Nilai Appetite (appet)", options=df['appet'].unique())
        pe = st.selectbox("Input Nilai Pedal Edema (pe)", options=df['pe'].unique())
        ane = st.selectbox("Input Nilai Anemia (ane)", options=df['ane'].unique())

    features = [bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]

    # Membuat button untuk memprediksi
    if st.button("Prediksi"):
        # Pastikan semua nilai input yang diambil adalah numerik (float atau int)
        features = [float(i) if isinstance(i, str) and i.replace('.', '', 1).isdigit() else i for i in features]
        
        prediction, score = predict(x, y, features)
        st.info("Prediksi Sukses...")

        if prediction == 1:
            st.warning("Pasien tersebut rentan terkena penyakit ginjal")
        else:
            st.success("Pasien tersebut relatif aman dari penyakit ginjal")

        st.write("Akurasi model: ", (score*100), "%")
