import streamlit as st
import pandas as pd

st.title('Labelling')

# Meminta pengguna mengunggah file dataset
uploaded_file = st.file_uploader("Unggah dataset komentar (format: CSV)", type=["csv"])

if uploaded_file is not None:
    # Membaca dataset menjadi DataFrame
    data = pd.read_csv(uploaded_file)

    # Menampilkan informasi tentang dataset
    st.write("Data komentar:")
    st.write(data)

    # Memeriksa nama kolom yang tersedia dalam DataFrame
    st.write("Comment")
    st.write(data.columns)

    # Menambahkan kolom baru untuk label
    data['Label'] = ''

    # Menampilkan kolom komentar dengan tombol plus dan minus
    st.session_state.comment_index = 0  # Inisialisasi indeks komentar

    if st.session_state.comment_index < len(data):
        st.write(f"Komentar ke-{st.session_state.comment_index + 1}: {data.iloc[st.session_state.comment_index]['Komentar']}")
        plus_clicked = st.button('Positive')
        minus_clicked = st.button('Negative')

        if plus_clicked:
            data.at[st.session_state.comment_index, 'Label'] = 'Positive'
            st.session_state.comment_index += 1  # Pindah ke komentar selanjutnya
        elif minus_clicked:
            data.at[st.session_state.comment_index, 'Label'] = 'Negative'
            st.session_state.comment_index += 1  # Pindah ke komentar selanjutnya

        # Tombol "Next" untuk melihat komentar selanjutnya
        if st.session_state.comment_index < len(data):
            next_clicked = st.button('Next')
            if next_clicked:
                st.session_state.comment_index += 1  # Pindah ke komentar selanjutnya

    # Menampilkan data setelah pengklasifikasian
    st.write("Data komentar setelah pengklasifikasian:")
    st.write(data)
