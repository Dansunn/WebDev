import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as component

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


sheet_id = "16gvv3Br49pD0HYy6qu3H5RdkKQRT1ObTxN4ALsNrRSI"
sheet_name = "JumlahPenduduk"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dfjmlpddk=pd.read_csv(url)

sheet_id = "16gvv3Br49pD0HYy6qu3H5RdkKQRT1ObTxN4ALsNrRSI"
sheet_name = "Kelahiran"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dfkelahiran=pd.read_csv(url)

sheet_id = "16gvv3Br49pD0HYy6qu3H5RdkKQRT1ObTxN4ALsNrRSI"
sheet_name = "Kematian"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dfkematian=pd.read_csv(url)

# Create a container for the main content
main_container = st.container()

# Add content to the main container
with main_container:
    st.write(' ')
    st.write(' ')

    st.markdown("<h1 style='text-align: center; color:black;'>Informasi Penduduk DKI Jakarta</h1>", unsafe_allow_html=True)

    first_choice = st.selectbox("First level options", ["Pilih Data","Jumlah Penduduk", "Kelahiran","Kematian"])

    if first_choice == 'Jumlah Penduduk':
        st.dataframe(dfjmlpddk)
       
    elif first_choice == 'Kelahiran':
        st.dataframe(dfkelahiran)
        
    elif first_choice == 'Kematian':
        st.dataframe(dfkematian)
        
