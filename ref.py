import streamlit as st
import datetime
import pandas as pd

# Mengatur tema
st.set_page_config(layout="wide", page_title="Kalkulator BMI Canggih", page_icon=":scales:")

# Ini adalah rumus perhitungan BMI
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

# Fungsi ini menerima nilai BMI dan mengembalikan rekomendasi 
# kesehatan berdasarkan kategori BMI.
def interpret_bmi(bmi):
    if bmi < 18.5:
        st.image('https://static.vecteezy.com/system/resources/previews/009/493/310/original/a-thin-red-haired-man-with-his-hands-on-his-waist-illustration-in-a-flat-cartoon-style-vector.jpg')
        return ("Underweight🥩🍴", 
                "Ayo, tingkatkan asupan makananmu dengan pilihan yang lebih banyak dan bernutrisi! Jadikan setiap suapan sebagai langkah cerdas menuju kesehatan yang lebih baik. Selalu ada ruang untuk lebih banyak kebaikan di piringmu!",
                "#3498db",
                [("Yoga", "Memperbaiki postur dan meningkatkan massa otot tanpa beban berlebih"),
                ("Berenang", "Melatih semua grup otot tanpa risiko cedera"),
                ("Berjalan cepat", "Meningkatkan kekuatan otot dengan risiko rendah")],
                "Setiap langkah kecil adalah kemajuan. Anda lebih kuat dari yang Anda pikir!")
    elif 18.5 <= bmi < 25:
        st.image('https://img.freepik.com/free-vector/hand-drawn-strong-man-cartoon-illustration_52683-117786.jpg?size=338&ext=jpg&ga=GA1.1.1369675164.1715385600&semt=ais_user')
        return ("Normal👌😉", 
                "Mari kita terus jaga semangat! Pertahankan pola makan sehat dan rutin berolahraga sebagai investasi terbaik untuk kesehatan jangka panjangmu. Ayo buat setiap hari sebagai langkah positif menuju versi terbaik dirimu!.",
                "#2ecc71",
                [("Berlari", "Membakar kalori dan meningkatkan kesehatan kardiovaskular"),
                ("Berenang", "Cardio yang efektif dan rendah risiko"),
                ("Latihan beban", "Membangun massa otot dan memperkuat tulang")],
                "Tetaplah konsisten dan nikmati prosesnya; Anda sedang melakukan hal-hal luar biasa untuk tubuh Anda!")
                
    elif 25 <= bmi < 30:
        st.image('https://static.vecteezy.com/system/resources/previews/022/699/171/non_2x/sad-fat-cute-man-illustration-in-cartoon-flat-style-concept-lifestyle-illness-and-overweight-vector.jpg')
        return ("Overweight🏃‍♂️🏊‍♂️", 
                "Ayo, mulai kurangi asupan kalori dan tingkatkan aktivitas fisikmu! Setiap langkah kecil yang kamu ambil membawa dampak besar bagi kesehatan dan kesejahteraanmu. Bersama, kita bisa menjalani hidup yang lebih sehat dan penuh energi!",
                "#f39c12",
                [("Berjalan kaki cepat", "Cardio ringan untuk memulai dan membakar kalori"),
                ("Berenang", "Mengurangi beban sendi saat berolahraga"),
                ("Aerobik air", "Menyenangkan dan efektif untuk menurunkan berat badan")],
                "Setiap langkah adalah langkah ke arah yang benar. Terus bergerak maju!")
    else:
        st.image('https://media.istockphoto.com/id/1517145949/vector/fat-man-stands-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=1HwF4ukEyJ-JK7QAnmMBD_Lto0tew9xGC-6sWQuJb38=')
        return ("Obese🏋️‍♂️🍴", 
                "Mulai Hari Ini - Ingat, perjalanan seribu mil dimulai dengan satu langkah. Tak peduli seberapa kecil, langkah pertama Anda menuju kesehatan yang lebih baik adalah yang paling penting!",
                "#e74c3c",
                [("Berjalan kaki", "Mulai dengan sesuatu yang mudah dan bertahap"),
                ("Latihan kekuatan", "Membantu membakar kalori bahkan saat istirahat"),
                ("Streching", "Latihan interval intensitas rendah untuk memulai tanpa risiko tinggi")],
                "Setiap hari membawa peluang baru untuk menjadi lebih baik. Jangan menyerah!")

# Menampilkan informasi terkait BMI dengan detail olahraga
def display_bmi_info(bmi):
    category, advice, color, exercises, motivation = interpret_bmi(bmi)
    st.success(f'BMI Anda adalah {bmi:.2f}.')
    st.metric(label="Kategori", value=category, delta_color="off", help=advice)
    st.caption(advice)
    st.markdown("**Saran Olahraga:**")
    for exercise, benefit in exercises:
        with st.expander(f"{exercise}"):
            st.markdown(f"**Manfaat:** {benefit}")
    st.markdown("**Motivasi:**")
    st.markdown(motivation)

# Pelacakan berat badan
def display_weight_tracking():
    st.subheader("Tracking Berat Badan🏋️‍♂️")
    if 'weight_data' not in st.session_state or st.session_state['weight_data'] is None:
        st.session_state['weight_data'] = pd.DataFrame(columns=['Tanggal', 'Berat'])
        
    with st.form("weight_form"):
        date = st.date_input("Tanggal")
        weight = st.number_input("Berat Badan (kg)", min_value=0.1)
        submit_button = st.form_submit_button("Tambah Data")
        if submit_button:
            new_data = pd.DataFrame({'Tanggal': [date], 'Berat': [weight]})
            st.session_state['weight_data'] = pd.concat([st.session_state['weight_data'], new_data], ignore_index=True)
            st.success("Data Berat Badan Ditambahkan")

    if st.session_state['weight_data'].empty:
        st.write("Belum ada data yang ditambahkan.")
    else:
        st.write(st.session_state['weight_data'])

# Fungsi utama
def main():
    # Menambahkan pilihan warna latar belakang
    background_color = st.sidebar.color_picker('Pilih Warna Latar Belakang', '#87CEEB')
    st.markdown(
        f"""
        <style>
        div.stApp {{
            background-color: {background_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
        
    st.markdown(
        """
        <style>
        @keyframes rainbow {
            0%{color: red;}
            15%{color: orange;}
            30%{color: yellow;}
            45%{color: green;}
            60%{color: blue;}
            75%{color: indigo;}
            90%{color: violet;}
            100%{color: red;}
        }
        .rainbow-text {
            animation: rainbow 5s infinite;
            font-size: 40px;  /* Mengatur ukuran font */
            font-weight: bold;  /* Membuat teks menjadi tebal */
        }
        </style>
        <p class='rainbow-text'>SELAMAT DATANG DI BMI KALKULATOR CANGGIH</p>
        """,
        unsafe_allow_html=True
    )
        
    st.markdown(
        """
        <style>
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {transform: translateY(0);}
            40% {transform: translateY(-30px);}
            60% {transform: translateY(-15px);}
        }
        .bounce-text {
            animation: bounce 2s infinite;
        }
        </style>
        <p class='bounce-text'>🏃‍♂️🏋️‍♂️🍴🥩👌🕛!</p>
        """,
        unsafe_allow_html=True
    )
        
    st.markdown(
        """
        <style>
        @keyframes pulse {
            0% {transform: scale(1);}
            50% {transform: scale(1.1);}
            100% {transform: scale(1);}
        }
        .pulse-text {
            animation: pulse 2s infinite;
        }
        </style>
        <p class='pulse-text'>Jaga Kesehatanmu dengan Kalkulator BMI!</p>
        """,
        unsafe_allow_html=True
    )
        
    def show_intro_video():
        st.video("https://www.youtube.com/watch?v=NJiw11hIKKM")

    st.title("")
    show_intro_video()  # Memanggil fungsi yang menampilkan video

    st.sidebar.header('Interactive BMI Calculator👌')
    st.sidebar.markdown("<hr style='border: 2px solid blue; border-radius: 5px;'/>", unsafe_allow_html=True)
        
    with st.sidebar.expander("Anggota Kelompok"):
        st.markdown(
            """
            <style>
            @keyframes slide-in {
                from {
                    transform: translateX(-100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            .slide-in-text {
                animation: slide-in 1s ease-out;
            }
            </style>
            <div class='slide-in-text'>
            - Elvio Aldwin Faqih (2320521)<br>
            - Indana Zulfa (2320531)<br>
            - Nayla Rahma (2320540)<br>
            - Pramesthi Dewi Amelia (2320543)<br>
            - Raden Kayla Syawal Sabira (2320547)
            </div>
            """,
            unsafe_allow_html=True
        )
        
    # Pastikan indentasi ini sesuai dengan konteks kode sebelumnya
    with st.sidebar.expander("Tentang Aplikasi Ini"):
        st.markdown("""
        <div style="text-align: justify;">
        <b>Aplikasi Kalkulator BMI Canggih</b> ini dirancang untuk memberikan pengalaman yang mudah, cepat, dan interaktif dalam menghitung serta memahami nilai <b>BMI (Body Mass Index)</b> Anda. Hanya dengan memasukkan berat dan tinggi badan, aplikasi ini akan mengolah data tersebut untuk memberikan hasil yang akurat.
        <br><br>
        Lebih dari sekedar penghitungan, aplikasi ini juga menyediakan <b>analisis mendalam</b> tentang kategori kesehatan Anda berdasarkan BMI, dilengkapi dengan <b>saran olahraga</b>. Selain itu, kami menyertakan <b>kata-kata motivasi</b> yang inspiratif untuk mendorong Anda dalam menjalani gaya hidup sehat.
        <br><br>
        Gunakan aplikasi ini sebagai langkah pertama Anda menuju perjalanan kesehatan yang lebih baik!
        </div>
        """, unsafe_allow_html=True)
        
    # Data untuk tabel BMI
    df = pd.DataFrame({
        "Kategori": ["Underweight", "Normal", "Overweight", "Obese"],
        "Min BMI": [0, 18.5, 25, 30],
        "Max BMI": [18.5, 24.99, 29.99, 60]
    })

    with st.sidebar.expander("Tabel Rentang BMI"):
        st.table(df)

    # Layout dengan kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Kalkulator BMI")
        weight = st.number_input("Berat (kg)", min_value=1.0, format="%.2f")
        height = st.number_input("Tinggi (cm)", min_value=1.0, format="%.2f")
        bmi = 0  # Nilai default untuk BMI
        if st.button('Hitung BMI'):
            bmi = calculate_bmi(weight, height)
            st.write(f"BMI Anda adalah {bmi:.2f}")
            display_bmi_info(bmi)  # Menampilkan informasi BMI termasuk saran diet dan motivasi

    
    # Menambahkan komponen eksternal
    st.markdown("## Data Tracking")
    display_weight_tracking()

if __name__ == '__main__':
    main()
