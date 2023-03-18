import streamlit as st
import pandas as pd
import numpy as np

st.subheader("Daniel - 32200023")


st.text_input("Masukkan Nama Anda", key="name")
st.write("Selamat Datang, ", st.session_state.name)

st.write("Masukkan Umur Anda")
x = st.slider('x')
st.write('Umur anda adalah', x)


st.write("Centang Box Untuk Menampilkan Dataframe")
if st.checkbox('Tampilkan Dataframe'):
    data = {'Nama Pemain' : ['Luka Doncic', 'Klay Thompson', 'Kevin Durant', 'James Wiseman', 'Demar DeRozan'],
            'No. Punggung' : [77, 11, 35, 00, 11],
            'Team NBA' : ['Dallas Mavericks', 'Golden State Warriors', 'Phoenix Suns', 'Detroit Pistons', 'Chicago Bulls']}
    chart_data = pd.DataFrame(data)
    chart_data

    

df = pd.DataFrame({
    'first column': ['Arsenal', 'Liverpool', 'Man. United', 'Man. City', 'Chelsea', 'Brighton', 'Newcastle United','Lainnya']
    })

option = st.selectbox(
    'Tim Premier League mana yang anda sukai?',
     df['first column'])

'Anda Memilih : ', option
