import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

st.set_page_config(
    page_title="Tugas 3 WebDev Phyton",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Tugas 3 Phyton WebDev - Daniel / 32200023")

#1. Write and Magic
st.title("(1. Write And Magic)")
st.write("Ini Contoh text saya")
("Ini Contoh text saya dengan magic")

#2. Text Element
st.title("(2. Text Element)")
st.header("Ini contoh header")
st.subheader("Ini contoh subheader")
st.caption("Ini contoh caption")

#3. Data Display Element
st.title("(3. Data Display Element)")
data = {'Tinggi' : [10, 8, 6, 8, 4],
        'Lebar' : [8, 6, 9, 4, 5],
        'Panjang' : [7, 8, 4, 5, 9]}
st.write(data)

#4. Chart Element
st.title("(4. Chart Element)")
chart_data = pd.DataFrame(data, index=['Balok 1', 'Balok 2', 'Balok 3', 'Balok 4', 'Balok 5'])
chart_data.head()

st.line_chart(chart_data)
st.bar_chart(chart_data)

# 5. Input Widget
name = st.text_input("Masukkan Nama Anda")
st.write("Selamat Datang, ",name)

st.write("Masukkan Umur Anda")
x = st.slider('x')
st.write('Umur anda adalah', x)

makanan = st.radio("Pilih Makanan Favorit Anda",('Pizza', 'Indomie','Bakso','dll'))
if makanan == 'Pizza':
    st.write('Anda Memilih Pizza.')
elif makanan == 'Indomie':
    st.write('Anda Memilih Indomie')
elif makanan == 'Bakso':
    st.write('Anda Memilih Bakso.')
else:
    st.write('Anda Labil.')

# 6. Media Elements
st.title("(6. Media Elements)")
img = Image.open("D:\File Penting\Dansunn\Kuliah\Semester 6\WebDev Phyton\Gojou.jpg")
st.image(img, caption="Gojou Satoru")

#7. Layout and Containers
st.title("(7. Layout and Containers)")
add_selectbox = st.sidebar.selectbox(
    "Media Sosial Kesukaan anda ?",
    ("Instagram", "Facebook", "Tiktok","Dll")
)

#8. Status Elements
st.title("(8. Status Elements)")
st.error("Menampilkan Pesan Error")
st.warning("Menampilkan Pesan Peringatan")
st.success("Menampilkan Pesan Berhasil")
st.info("Menampilkan Pesan Informasi")

#9. Control FLow
st.title("(9. Control Flow)")
with st.form("contoh_form"):
    st.write("Isi dalam form")
    sv = st.slider("Angka Kesukaan Anda")
    cv = st.checkbox("Centang Dulu Bos")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Angka Anda Adalah ", sv, "checkbox", cv)

#10. Utilities
st.title("(10. Utilities)")
st.help(pd.DataFrame)