import streamlit as st
import pandas as pd
import numpy as np

st.write("Daniel - 32200023")
st.subheader("Tugas 2 - Line Chart, Widgets, and Layout")

st.title("Line Chart and Bar Chart")
data = {'Tinggi' : [10, 8, 6, 8, 4],
        'Lebar' : [8, 6, 9, 4, 5],
        'Panjang' : [7, 8, 4, 5, 9]}
chart_data = pd.DataFrame(data, index=['Balok 1', 'Balok 2', 'Balok 3', 'Balok 4', 'Balok 5'])
chart_data.head()

st.line_chart(chart_data)
st.bar_chart(chart_data)

st.title("Widgets")
name = st.text_input("Masukkan Nama Anda")
st.write("Selamat Datang",name)

st.write("Masukkan Umur Anda")
x = st.slider('x')
st.write(x, 'Umur anda adalah', x)


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

st.title("Layout")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")



st.write("5C: Show progress")
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'