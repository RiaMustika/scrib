import streamlit as st
import numpy as np

from sklearn import datasets

st.title('Aplikasi Web Data Mining')
st.write("""
#Menggunakan beberapa algoritma dan dataset yang berbeda,
Mana yang terbaik???
""")

nama_dataset = st.sidebar.selectbox(
    'Pilih Dataset',
    ('BBC News Indonesia', 'Kompas.com', 'TV One News', 'CCN Indonesia', 'Serambinews')
)

st.write(f"##Dataset{nama_dataset}")

algoritma = st.sidebar.selectbox(
    'Pilih Algoritma',
    ('Random Forest', 'Naive Bayes')
)

st.write(f"##Algoritma{algoritma}")

def proses_data(nama):
    if nama == 'Posts':
        # Lakukan sesuatu untuk Posts
        print('Mengolah data Posts')
    elif nama == 'Comments':
        # Lakukan sesuatu untuk Comments
        print('Mengolah data Comments')
    else:
        # Lakukan sesuatu untuk kondisi lainnya
        print('Jenis data tidak diketahui')

# Memanggil fungsi dengan nilai 'Comments'
proses_data('Comments')