import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as component
from gsheetsdb import connect

from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
     .stApp { bottom: 150px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Coat_of_arms_of_Jakarta.svg/220px-Coat_of_arms_of_Jakarta.svg.png',
              width=px(50), height=px(50)),
        br(),
        link("https://twitter.com/ChristianKlose3", "Home"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Jelajah"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Tentang Jakarta"),
        br(),
        link("https://twitter.com/ChristianKlose3", "Informasi Covid-19"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Profil Pemerintahan"),
        "-||-",
        link("https://twitter.com/ChristianKlose3", "Informasi Penduduk"),
    ]
    layout(*myargs)
    


if __name__ == "__main__":
    footer()

# Create a container for the header
header_container = st.container()

# Add content to the header container
with header_container:
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img = Image.open("D:\File Penting\Dansunn\Kuliah\Semester 6\WebDev Phyton\LogoDKI.jpg")
        st.image(img)

    with col2:
        st.markdown("<h1 style='text-align: center; color:black;'>Website DKI Jakarta</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color:black;'>Sukses Jakarta Untuk Indonesia</h4>", unsafe_allow_html=True)

    with col3:
        st.write(" ")


sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K2=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K3=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2020K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2020K4=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K1=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K2=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
pd.options.display.max_rows = 9999
df2021K3=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2021K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2021K4=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K1=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K2"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K2=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K3"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K3=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2022K4"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2022K4=pd.read_csv(url)

sheet_id = "1gSmw9VYFViRO-FId4SN9wOHPMk6Yb8gi31ioKD1D1-A"
sheet_name = "2023K1"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df2023K1=pd.read_csv(url)

# Create a container for the main content
main_container = st.container()

# Add content to the main container
with main_container:
    st.write(' ')
    st.write(' ')

    st.markdown("<h1 style='text-align: center; color:black;'>Informasi Covid-19 DKI Jakarta</h1>", unsafe_allow_html=True)

    first_choice = st.selectbox("First level options", ["Pilih Data","2020K2", "2020K3","2020K4", "2021K1", "2021K2", "2021K3", "2021K4", "2022K1", "2022K2", "2022K3", "2022K4", "2023K1"])

    if first_choice == '2020K2':
        st.write(df2020K2)

    elif first_choice == '2020K3':
        st.write(df2020K3)

    elif first_choice == '2020K4':
        st.write(df2020K4)

    elif first_choice == '2021K1':
        st.write(df2021K1)

    elif first_choice == '2021K2':
        st.write(df2021K2)

    elif first_choice == '2021K3':
        st.write(df2021K3)

    elif first_choice == '2021K4':
        st.write(df2021K4)

    elif first_choice == '2022K1':
        st.write(df2022K1)

    elif first_choice == '2022K2':
        st.write(df2022K2)

    elif first_choice == '2022K3':
        st.write(df2022K3)

    elif first_choice == '2022K4':
        st.write(df2022K4)
     
    elif first_choice == '2023K1':
        st.write(df2023K1)


