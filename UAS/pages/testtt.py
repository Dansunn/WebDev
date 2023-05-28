import pandas as pd
import streamlit as st

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K2=pd.read_csv(url)
df2020K2.set_index('Bulan', inplace=True)


sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K3=pd.read_csv(url)
df2020K3.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K4=pd.read_csv(url)
df2020K4.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K1=pd.read_csv(url)
df2021K1.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K2=pd.read_csv(url)
df2021K2.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K3=pd.read_csv(url)
df2021K3.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K4=pd.read_csv(url)
df2021K4.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K1=pd.read_csv(url)
df2022K1.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K2=pd.read_csv(url)
df2022K2.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K3=pd.read_csv(url)
df2022K3.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K4=pd.read_csv(url)
df2022K4.set_index('Bulan', inplace=True)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2023K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2023K1=pd.read_csv(url)
df2023K1.set_index('Bulan', inplace=True)

first_choice = st.selectbox("First level options", ["Pilih Data","2020K2", "2020K3","2020K4", "2021K1", "2021K2", "2021K3", "2021K4", "2022K1", "2022K2", "2022K3", "2022K4", "2023K1"])
if first_choice == '2020K2':
        st.write(df2020K2)
        st.bar_chart(df2020K2)

elif first_choice == '2020K3':
        st.write(df2020K3)
