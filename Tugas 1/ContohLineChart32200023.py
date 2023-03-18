import streamlit as st
import pandas as pd
import numpy as np

st.write("Daniel - 32200023")
st.subheader("Contoh Line Chart dan Bar Chart")

data = {'Tinggi' : [10, 8, 6, 8, 4],
        'Lebar' : [8, 6, 9, 4, 5],
        'Panjang' : [7, 8, 4, 5, 9]}
chart_data = pd.DataFrame(data, index=['Balok 1', 'Balok 2', 'Balok 3', 'Balok 4', 'Balok 5'])
chart_data.head()

st.line_chart(chart_data)
st.bar_chart(chart_data)