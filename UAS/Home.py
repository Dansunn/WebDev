import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as component


from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def main():
    # Sidebar navigation
    page = st.sidebar.selectbox("Navigation", ("Profil Pemerintahan", "Jelajah", "Informasi Covid"))

if __name__ == "__main__":
    main()

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
        img = Image.open("./UAS/LogoDKI.jpg")
        st.image(img)

    with col2:
        st.markdown("<h1 style='text-align: center; color:black;'>Website DKI Jakarta</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center; color:black;'>Sukses Jakarta Untuk Indonesia</h4>", unsafe_allow_html=True)

    with col3:
        st.write(" ")

# Create a container for the main content
main_container = st.container()

# Add content to the main container
with main_container:
    st.write(' ')
    st.write(' ')

    tab1, tab2, tab3 = st.tabs(["Berita 1", "Berita 2", "Berita 3"])

    with tab1:
            st.header("HUT Ke-496 Kota Jakarta : Jadi Karya Untuk Nusantara")
            st.image("https://www.jakarta.go.id/uploads/contents/content--20230516015709.jpeg", width=600)
            st.markdown("<p style='text-align: justify; color:black;'>Diperingati tiap tanggal 22 Juni, tahun ini Jakarta akan segera mencapai usia ke-496. Dengan tema “Jadi Karya untuk Nusantara”, bersama kita sukseskan transisi Jakarta dari Ibu Kota Negara menjadi Kota Bisnis berskala global.</h1>", unsafe_allow_html=True)

    with tab2:
            st.header("Mengawal Capaian Tiga Pilar Utama Keketuaan ASEAN 2023")
            st.image("https://www.jakarta.go.id/uploads/pages/page-asean-matters-epicentrum-of-growth-tekad-indonesia-mengawal-capaian-tiga-pilar-utama-keketuaan-asean-2023-20230508084829.png", width=500)
            st.markdown("<p style ='text-align: justify; color:black;'>Dalam momentum Keketuaan ASEAN 2023, Indonesia bertekad memperkuat relevansi ASEAN dalam merespons tantangan kawasan dan global. Mari kita kawal bersama prioritas Indonesia untuk ASEAN 2023.</h1>", unsafe_allow_html=True)
            

    with tab3:
            st.header("Surveilans Dinas Kesehatan Provinsi DKI Jakarta")
            st.image("https://www.jakarta.go.id/uploads/pages/page-surveilans-dinas-kesehatan-provinsi-dki-jakarta-20230516111535.jpeg", width=500)
            st.markdown("<p style='text-align: justify; color:black;'>Dalam rangka penyelenggaraan upaya pemberantasan dan penanggulangan penyakit menular dan penyakit tidak menular diperlukan dukungan data-data dan informasi melalui suatu sistem surveilans epidemiologi penyakit secara rutin dan terpadu.</h1>", unsafe_allow_html=True)

            
st.markdown("<h1 style='text-align: center; color:black;'>Visi & Misi Kota Jakarta</h1>", unsafe_allow_html=True)

col1, col2 =st.columns(2)

with col1:
    img = Image.open("./UAS/Visi.jpg")
    st.image(img)

with col2:
    img = Image.open("./UAS/Misi.jpg")
    st.image(img)
