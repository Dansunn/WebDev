import streamlit as st
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
    st.markdown("<h1 style='text-align: center; color:black;'>Destinasi Wisata Populer</h1>", unsafe_allow_html=True)
    st.markdown('### 1. Monumen Nasional')
    img = Image.open("./UAS/Monas.jpg")
    st.image(img)
    st.markdown("<p style='text-align: justify; color:black;'>Monas atau Monumen Nasional merupakan icon kota Jakarta. Terletak di pusat kota Jakarta, menjadi tempat wisata dan pusat pendidikan yang menarik bagi warga Jakarta dan sekitarnya. Monas didirikan pada tahun 1959 dan diresmikan dua tahun kemudian pada tahun 1961. Monas selalu ramai dikunjungi wisatawan untuk melihat keindahan kota Jakarta dari puncak Monas, menambah wawasan sejarah Indonesia di ruang diorama ataupun menikmati segarnya hutan kota seluas kira-kira 80 hektar di tengah kota Jakarta.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Setiap hari libur, Monas selalu dikunjungi banyak wisatawan. Di sini Anda bisa menikmati banyak jenis wisata dan bahan pendidikan. Anda bisa menaiki monumen yang menjulang tinggi hingga ke puncak Monas. Anda juga dapat berolahraga bersama teman dan keluarga. Anda juga bisa menikmati taman yang indah dengan berbagai pepohonan yang rimbun dan asri. Atau Anda bisa menikmati hiburan air mancur yang menarik.</p>", unsafe_allow_html=True)
    
    st.markdown('### 2. Taman Mini Indonesia Indah')
    img = Image.open("./UAS/TMII.jpg")
    st.image(img)
    st.markdown("<p style='text-align: justify; color:black;'>Taman Mini Indonesia Indah (TMII) merupakan suatu kawasan taman wisata bertema budaya Indonesia di Jakarta Timur. Area seluas kurang lebih 150 hektar[1] atau 1,5 kilometer persegi ini terletak pada koordinat 6 derajat 18'6.8''LS, 106 derajat 53'47.2''BT. Di Indonesia, hampir setiap suku bangsa memiliki bentuk dan corak bangunan yang berbeda, bahkan tidak jarang satu suku bangsa memiliki lebih dari satu jenis bangunan tradisional. Bangunan atau arsitektur tradisional yang mereka buat selalu dilatarbetakangi oleh kondisi lingkungan dan kebudayaan yang dimiliki. Di TMII, gambaran tersebut diwujudkan melalui Anjungan Daerah, yang mewakili suku-suku bangsa yang berada di 33 Provinsi Indonesia. Anjungan provinsi ini dibangun di sekitar danau dengan miniatur Kepulauan Indonesia, secara tematik dibagi atas enam zona; Jawa, Sumatera, Kalimantan, Sulawesi, Bali dan Nusa Tenggara, Maluku dan Papua. Tiap anjungan menampilkan bangunan khas setempat.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Taman ini merupakan rangkuman kebudayaan bangsa Indonesia, yang mencakup berbagai aspek kehidupan sehari-hari masyarakat 33 provinsi Indonesia (pada tahun 1975) yang ditampilkan dalam anjungan daerah berarsitektur tradisional, serta menampilkan aneka busana, tarian dan tradisi daerah.</p>", unsafe_allow_html=True)
   
    st.markdown('### 3. Taman Margasatwa Ragunan')
    img = Image.open("./UAS/Ragunan.jpg")
    st.image(img)
    st.markdown("<p style='text-align: justify; color:black;'>Sebuah taman seluas 147 hektar dan berpenghuni lebih dari 2.009 ekor satwa serta ditumbuhi lebih dari 20.000 pohon membuat suasana lingkungannya sejuk dan nyaman. Lahannnya tertata dan terbangun serta sebagian lagi masih dikembangkan menuju suatu kebun binatang yang modern sebagai identitas kota Jakarta.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Berkunjung ke Taman Margasatwa Ragunan berarti memasuki sebuah hutan tropis mini, di dalamnya terdapat keanekaragaman hayati yang memiliki nilai konservasi tinggi dan menyimpan harapan untuk masa depan.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Sebuah kebun binatang modern menampilkan suatu system ekologi yang lengkap yang bias menjadi satu sumber ilmu pengetahuan yang akan mengawali langkah pelestarian kehidupan alam liar. Singkatnya, kebun binatang adalah “Kapal Nuh” kita dalam menghadapi bencana dan kerusakan alam yang akhir-akhir ini sering terjadi. Bila nanti sudah tidak ada lagi hutan di bumi ini, paling tidak masih ada contoh-contoh makhluk yang menakjubkan ini di kebun binatang, entah itu telah berwujud satwa ataupun masih berbentuk embrio, sel atau DNA.</p>", unsafe_allow_html=True)
    
    st.markdown('### 4. Dst')



st.text(" ")
st.text(" ")
st.text(" ")


# Create a container for the footer
footer_container = st.container()

# Add content to the footer container
with footer_container:
    st.write('© 2023 My Website. All rights reserved.')
    st.write('Powered by Streamlit.')
