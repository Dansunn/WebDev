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
        img = Image.open("D:\File Penting\Dansunn\Kuliah\Semester 6\WebDev Phyton\LogoDKI.jpg")
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

    st.markdown("<h3 style='text-align: center; color:black;'>Kota DKI Jakarta</h3>", unsafe_allow_html=True)
    img = Image.open("D:\\File Penting\\Dansunn\Kuliah\\Semester 6\\WebDev Phyton\\NightDKI.jpg")
    st.image(img)
    st.markdown("<p style='text-align: justify; color:black;'>Jakarta adalah nama Ibu Kota Republik Indonesia. Provinsi DKI Jakarta terbagi menjadi lima wilayah Kota Administrasi dan satu Kabupaten Administratif, yakni: Kota Administrasi Jakarta Pusat dengan luas 47,90 km2, Jakarta Utara dengan luas 142,20 km2, Jakarta Barat dengan luas 126,15 km2, Jakarta Selatan dengan luas 145,73 km2, Jakarta Timur dengan luas 187,73 km2, serta Kabupaten Administratif Kepulauan Seribu dengan luas 11,81 km2. Di sebelah utara membentang pantai sepanjang 35 km yang menjadi muara 13 sungai dan dua kanal. Di sebelah selatan dan timur berbatasan dengan Kota Depok, Kabupaten Bogor, Kota Bekasi dan Kabupaten Bekasi, sebelah barat dengan Kota Tangerang dan Kabupaten Tangerang, serta di sebelah utara dengan Laut Jawa.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Secara geologis, seluruh dataran terdiri dari endapan pleistocene yang terdapat pada ±50 m di bawah permukaan tanah. Bagian selatan terdiri atas lapisan alluvial, sedangkan dataran rendah pantai merentang ke bagian pedalaman sekitar 10 km. Di bawahnya terdapat lapisan endapan yang lebih tua yang tidak tampak pada permukaan tanah, karena tertimbun seluruhnya oleh endapan alluvium. Di wilayah bagian utara terdapat endapan tersebut pada kedalaman 10-25 m, makin ke selatan permukaan keras semakin dangkal hingga 8-15 m. Pada bagian tertentu juga terdapat lapisan permukaan tanah yang keras dengan kedalaman 40 m.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Keadaan Kota Jakarta umumnya beriklim panas dengan suhu udara maksimum berkisar 32,7°C-34,°C pada siang hari, dan suhu udara minimum berkisar 23,8°C-25,4°C pada malam hari. Rata-rata curah hujan sepanjang tahun 237,96 mm, selama periode 2002-2006 curah hujan terendah sebesar 122,0 mm terjadi pada 2002 dan tertinggi sebesar 267,4 mm terjadi pada 2005, dengan tingkat kelembaban udara mencapai 73,0-78,0 persen serta kecepatan angin rata-rata mencapai 2,2 m/detik-2,5 m/detik.</p>", unsafe_allow_html=True)

    st.write(' ')
    st.write(' ')

    st.markdown("<h3 style='text-align: center; color:black;'>Sejarah</h3>", unsafe_allow_html=True)
    img = Image.open("D:\File Penting\Dansunn\Kuliah\Semester 6\WebDev Phyton\OldDKI.jpg")
    st.image(img)
    st.markdown("<p style='text-align: justify; color:black;'>Sebagai kota pelabuhan, Jakarta pada mulanya bernama Sunda Kelapa. Kemudian, pada 22 Juni 1527, Pangeran Fatahillah datang dan mendirikan kota Jayakarta untuk mengganti Sunda Kelapa. Tanggal inilah yang kemudian ditetapkan sebagai saat berdiri kota Jakarta. Kota Jayakarta berkembang sebagai kota pelabuhan yang sibuk, di mana para pedagang dari Cina, India, Arab, Eropa, serta negara-negara lain saling bertukar komoditas.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Pada 1619, VOC Belanda yang dipimpin Jan PieterszoonCoen menghancurkan Jayakarta, lalu membangun kota baru di bagian barat sungai Ciliwung yang dinamakan Batavia, diambil dari Batavieren, nenek moyang bangsa Belanda. Batavia direncanakan dan dibangun nyaris mirip dengan kota-kota di Belanda, yaitu dalam bentuk blok yang masing-masing dipisahkan oleh kanal, dilindungi oleh dinding sebagai benteng, serta parit. Selesai dibangun pada 1650, Batavia adalah tempat tinggal bangsa Eropa. Sementara bangsa Cina, Jawa, dan penduduk pribumi lainnya disingkirkan ke tempat lain. Batavia digunakan untuk menyebut nama kota ini selama tiga abad lebih. Setidaknya bermula pada 1619, atau sumber lain mengatakan tahun 1621, hingga 1942. Sejalan dengan kebijakan de-Nederlandisasi oleh Pemerintah Jepang, nama kota sengaja diganti dengan bahasa Indonesia atau Jepang. Walhasil, pada 1942, nama Batavia berubah menjadi Djakarta sebagai akronim Djajakarta.  </p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Menurut Lasmijah Hardi dalam Jakartaku, Jakartamu, Jakarta Kita (1987), pergantian nama itu bertepatan dengan perayaan Hari Perang Asia Timur Raya, pada 8 Desember 1942. Nama lengkap kota itu ialah Jakarta Tokubetsu Shi. Setelah Jepang kalah pada Perang Dunia II dan Indonesia merdeka pada 17 Agustus 1945, nama Jakarta tetap dipakai dengan meninggalkan nama Jepang-nya. Memasuki zaman Indonesia merdeka, Menteri Penerangan Republik Indonesia Serikat (RIS) saat itu, Arnoldus Isaac Zacharias Mononutu, menegaskan, sejak 30 Desember 1949 tak ada lagi sebutan Batavia bagi kota ini. Sejak saat itu, nama Ibu Kota Republik Indonesia adalah Jakarta. Pemberian nama Jakarta ini kembali dikukuhkan pada 22 Juni 1956 oleh Wali Kota Jakarta Sudiro (1953-1960). Saat itu, sebelum 1959, posisi Jakarta masih merupakan bagian dari Provinsi Jawa Barat. Pada 1959, status Jakarta diubah, dari sebuah kotapraja di bawah wali kota ditingkatkan menjadi Daerah Tingkat Satu yang dipimpin gubernur. Gubernur pertama ialah Soemarno Sosroatmodjo. Pada 1961, status Jakarta diubah kembali, dari Daerah Tingkat Satu menjadi Daerah Khusus Ibu Kota (DKI).</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify; color:black;'>Sedangkan penetapan tanggal lahir Jakarta didasarkan pada momen peristiwa kemenangan Fatahillah mengusir Portugis dari Sunda Kelapa pada 22 Juni 1527. Seperti diketahui, untuk memperingati momen itu, nama Sunda Kelapa kemudian diubah menjadi Jayakarta. Hingga kini, setiap 22 Juni diperingati sebagai HUT Ibu Kota Republik Indonesia.</p>", unsafe_allow_html=True)
