import streamlit as st

# Mengatur warna latar belakang dan warna teks
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ff0000;  /* Kode warna hex untuk merah */
        color: #ffffff;             /* Kode warna hex untuk putih */
    }
    .css-1d391kg {
        color: #ffffff;             /* Mengatur warna teks untuk elemen tertentu */
    }
    table {
        border: 2px solid white;    /* Garis tabel berwarna putih */
    }
    th {
        background-color: #ff6347;  /* Warna latar untuk header tabel */
        color: white;               /* Warna teks untuk header tabel */
    }
    td {
        background-color: #ffe4e1;  /* Warna latar untuk sel tabel */
        color: black;               /* Warna teks untuk sel tabel */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menentukan nilai kolesterol dalam bahan pangan
cholesterol_values = {
    'Daging dan Unggas': {'Daging kambing': 71, 'Daging sapi': 70, 'Daging ayam': 63, 'Daging bebek': 65, 'Daging babi': 80,
                          'Daging anjing': 44.4, 'Daging kalkun': 77, 'Daging unta': 61},
    'Ikan': {'Ikan tuna': 45, 'Ikan salmon': 48, 'Ikan lele': 60, 'Ikan mujair': 55, 'Ikan tongkol': 60, 'Ikan gurame': 66,
             'Ikan patin': 39},
    'Susu dan Telur': {'Susu sapi': 250, 'Telur': 155, 'Mentega': 215, 'Yogurt': 45, 'Kuning telur': 550, 'Keju': 140},
    'Makanan lainnya': {'Sosis daging': 150, 'Hamburger': 47, 'Seblak': 121, 'Bakso': 74, 'Kebab': 79, 'Coklat': 290}
}

# Fungsi untuk menghitung kolesterol
def calculate_cholesterol(jenis_makanan, nama_makanan, bobot):
    if jenis_makanan in cholesterol_values and nama_makanan in cholesterol_values[jenis_makanan]:
        cholesterol_per_100g = cholesterol_values[jenis_makanan][nama_makanan]
        total_cholesterol = (cholesterol_per_100g / 100) * bobot
        return total_cholesterol
    else:
        return f"Tidak ada data kolesterol untuk {nama_makanan} dalam kategori {jenis_makanan}."

# Fungsi untuk evaluasi resiko kolesterol
def evaluate_risk(total_cholesterol):
    if total_cholesterol < 200:
        return "Risiko kolesterol rendah."
    elif 200 <= total_cholesterol < 240:
        return "Risiko kolesterol sedang."
    else:
        return "Risiko kolesterol tinggi."

# Bagian Depan Aplikasi
st.title('Cholesterol Calculator For Foods🥩')  

st.markdown('''Cholesterol Calculator For Foods digunakan untuk menyajikan tabel makanan beserta jumlah kolesterol, menghitung kandungan kolesterol berdasarkan bobot makanan,
             serta memberikan saran makanan sehat.
            ☆: .｡. o(≧▽≦)o .｡.:☆''')
st.markdown('---')

# Sidebar navigation
with st.sidebar:
    selected = st.sidebar.selectbox('Menu', ['Perkenalan dan Penjelasan Singkat', 'Daftar Makanan', 'Perhitungan Kolesterol', 'Menu Interaktif'])

if selected == 'Perkenalan dan Penjelasan Singkat':
    st.markdown('KELOMPOK 7 (1E-PMIP):')
    st.write('''
    1. Kalisa Khatelya (2320532)
    2. Nayla Shafa Aulia (2320541)
    3. Selvi Wardayanti (2320555)
    4. Syifa Aprilya (2320558)
    5. Zikri (2320562)''')

    st.header('💡 Tahukah Anda??', divider='rainbow')
    st.write('''
            Bahwa sama sekali tidak ada kolesterol dalam makanan nabati apa pun, 
            termasuk sereal, buah-buahan, sayuran, dan biji-bijian? 
            Kolesterol hanya berasal dari makanan hewani🐓🐄''')
    st.write('''
                Kalkulator kolesterol adalah alat yang dapat membantu kita untuk mengetahui berapa 
                banyak kolesterol dalam makanan yang kita makan. Dengan kalkulator kolesterol ini, 
                kita dapat dengan cepat menentukan asupan kolesterol harian dan melacaknya. Seseorang 
                yang berisiko terkena penyakit jantung harus menjaga konsumsi kolesterol hariannya 
                sekitar 200 mg.''')

elif selected == 'Daftar Makanan':
    st.header('🧀🍖Daftar Makanan🍔🥚')
    st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
    st.markdown('''Menu ini menyajikan daftar makanan beserta jumlah kolesterolnya setiap bobot per 100 gram dalam satuan mg. Tabel Makanan ini berfungsi untuk memberikan informasi
             kepada pengguna tentang berapa jumlah kolesterol dalam bahan pangan, ini disajikan dalam bobot per 100 gram makanan.
             Untuk mengetahui jumlah kolesterol dalam bobot makanan yang kalian inginkan, silahkan klik menu perhitungan kolesterol ya!!''')
    jenis_makanan = st.selectbox("Pilih Bahan Pangan:", ["Daging dan Unggas", "Ikan", "Susu dan Telur", "Makanan Lainnya"])
    if jenis_makanan == "Daging dan Unggas":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Daging Kambing|71                    |
                |Daging Sapi   |70                    |
                |Daging Ayam   |63                    |
                |Daging Bebek  |65                    |
                |Daging Babi   |80                    |
                |Daging Anjing |44,4                  |
                |Daging Kalkun |77                    |
                |Daging Unta   |61                    |
                  ''')  
    if jenis_makanan == "Ikan":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Ikan Tuna     |45                    |
                |Ikan Salmon   |48                    |
                |Ikan Lele     |60                    |
                |Ikan Mujair   |55                    |
                |Ikan Tongkol  |60                    |
                |Ikan Gurame   |66                    |
                |Ikan Patin    |39                    |         
                ''')
    if jenis_makanan == "Susu dan Telur":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Susu Sapi     |250                   |
                |Telur         |155                   |
                |Mentega       |215                   |
                |Yoghurt       |45                    |
                |Kuning Telur  |550                   |
                |Keju          |140                   |        
                ''')
    if jenis_makanan == "Makanan Lainnya":
        st.markdown('''
                | Nama Makanan |Jumlah Kolesterol (mg)|
                |--------------|----------------------|
                |Sosis Daging  |150                   |
                |Hamburger     |47                    |
                |Seblak        |121                   |
                |Bakso         |74                    |
                |Kebab         |79                    |
                |Coklat        |290                   |        
                ''')    

elif selected == 'Perhitungan Kolesterol':
    st.header('Perhitungan Kolesterol Dalam Makanan🧮🍳', divider='red')
    st.markdown('Nah, di sini Anda dapat memilih jenis bahan pangan, jenis makanan, serta bobot yang ingin Anda ketahui jumlah kolesterolnya dalam makanan tersebut.')
    st.markdown('---')
    jenis_makanan = st.selectbox('Pilih Jenis Bahan Pangan', list(cholesterol_values.keys()))
    makanan_list = list(cholesterol_values[jenis_makanan].keys()) # List makanan berdasarkan jenis makanan yang dipilih
    nama_makanan = st.selectbox('Pilih jenis makanan', makanan_list)
    bobot = st.number_input('Masukkan bobot yang diinginkan (gram)', min_value=1, value=100)

    if st.button('Hitung Kolesterol'):
        total_cholesterol = calculate_cholesterol(jenis_makanan, nama_makanan, bobot)
        if isinstance(total_cholesterol, str):
            st.error(total_cholesterol)
        else:
            st.success(f'Perkiraan kolesterol dalam {nama_makanan} ({bobot}g): {total_cholesterol} mg')
            st.balloons()
            st.markdown('---')
            st.header('Saran Makanan', divider='blue')
            if total_cholesterol < 200:
                st.write("Hore! Kolesterol dalam makanan Anda rendah. Ini adalah beberapa saran untuk menjaga kesehatan dan mengatur pola makan Anda:")
                st.write("- Pilih lebih banyak buah-buahan dan sayuran segar untuk menu sehari-hari.")
                st.write("- Rasakan kelezatan ikan dan kacang-kacangan sebagai sumber protein yang lebih sehat.")
                st.write("- Batasi makanan olahan dan makanan cepat saji yang tinggi lemak.")
                st.write("- Tetap aktif! Berjalan-jalan, bersepeda, atau lakukan olahraga ringan setiap hari.")
            elif 200 <= total_cholesterol < 240:
                st.write("Hmm, kolesterol dalam makanan Anda sedang. Ini adalah beberapa saran untuk menjaga kesehatan dan mengatur pola makan Anda:")
                st.write("- Pilih makanan rendah lemak dan tinggi serat seperti oatmeal dan buah-buahan.")
                st.write("- Coba hidangkan ikan alih-alih daging merah untuk variasi yang lebih sehat.")
                st.write("- Tetap aktif! Lakukan aktivitas fisik yang Anda nikmati setiap hari.")
                st.write("- Jika Anda merasa perlu, konsultasikan dengan dokter untuk evaluasi lebih lanjut.")
            else:
                st.write("Oh tidak! Kolesterol dalam makanan Anda tinggi. Tapi jangan khawatir, ini adalah beberapa saran untuk memulai perubahan:")
                st.write("- Batasi makanan tinggi lemak jenuh seperti daging berlemak dan produk olahan susu.")
                st.write("- Cari sumber protein rendah lemak seperti tahu dan ayam tanpa kulit.")
                st.write("- Hindari makanan cepat saji dan camilan tinggi lemak.")
                st.write("- Aktivitas fisik adalah kunci! Cobalah berjalan kaki atau berenang untuk memulai.")
                st.write("- Jika perlu, temui dokter untuk rencana pengelolaan yang lebih spesifik.")


elif selected == 'Menu Interaktif':
    st.header('Menu Interaktif 🍽', divider='blue')

    st.subheader('Tes Pengetahuan 📝')
    st.write('''Yuk, tes pengetahuan tentang kolesterol akan mengasah pengetahuanmu tentang kesehatan! Ayo, kita jelajahi beberapa pertanyaan seru seputar kolesterol!''')
    st.write('1. Apa yang dimaksud dengan kolesterol HDL?')
    answer1 = st.radio('1.', options=['A. Kolesterol Baik', 'B. Kolesterol Jelek', 'C. Kolesterol Total'])
    st.write('2. Makanan mana yang mengandung kolesterol tinggi?')
    answer2 = st.radio('2.', options=['A. Buah-buahan', 'B. Sayuran', 'C. Daging merah'])
    st.write('3. Bagaimana cara menurunkan kolesterol LDL?')
    answer3 = st.radio('3.', options=['A. Mengonsumsi makanan tinggi lemak', 'B. Berolahraga secara teratur', 'C. Minum minuman bersoda'])

    if st.button('Submit'):
        score = 0
        if answer1 == 'A. Kolesterol Baik':
            score += 1
        if answer2 == 'C. Daging merah':
            score += 1
        if answer3 == 'B. Berolahraga secara teratur':
            score += 1
        st.write(f'Nilai Anda: {score}/3')
        st.balloons()
    st.markdown(
            '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
            unsafe_allow_html=True
        )
    st.subheader('Resep Sehat 🥗')
    st.write('Ingin mencoba resep sehat rendah kolesterol? Lihat resep berikut ini:')
    st.write('- Salad sayur dengan dressing lemon')
    st.write('- Sosis sapi panggang dengan tumis sayuran')
    st.write('- Smoothie buah-buahan segar dengan yogurt rendah lemak')
