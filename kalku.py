import streamlit as st
import pandas as pd
import numpy as np

# Menambahkan CSS untuk mengubah warna latar belakang menjadi hijau muda
st.markdown(
    """
    <style>
    .stApp {
        background-color: #CDFFAC;
        color: black;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title(":fire: :red[Kalkulator Perhitungan Oksigen untuk Pembakaran Batubara]")

# Membuat tab
tab1, tab2, tab3 = st.tabs(["Home", "Informasi Lanjut", "Aplikasi"])

with tab1:
    st.subheader("Tentang aplikasi")
    st.write(f"Kalkulator Perhitungan Oksigen untuk Pembakaran Batubara adalah alat atau sistem perangkat lunak yang digunakan untuk menghitung kebutuhan oksigen yang diperlukan dalam proses pembakaran batubara.")
    
    st.subheader("Manfaat Kalkulator Kebutuhan Oksigen dan Udara Berlebih")
    st.write("""
    Kalkulator kebutuhan oksigen untuk pembakaran batubara dengan udara berlebih bermanfaat untuk berbagai aspek operasional dan efisiensi. Berikut adalah beberapa manfaat utama:

    1. Efisiensi Energi: Dengan mengoptimalkan penggunaan bahan bakar, kalkulator ini membantu memastikan bahwa batubara dibakar dengan efisien, sehingga memaksimalkan energi yang dihasilkan dari bahan bakar yang digunakan.

    2. Pengurangan Emisi: Menghitung dan mengontrol jumlah udara berlebih membantu mengurangi emisi gas berbahaya seperti CO2 dan NOx, yang berkontribusi pada pengurangan pencemaran udara dan dampak lingkungan.

    3. Pengelolaan Sumber Daya: Dengan mengatur penggunaan oksigen dan memantau kebutuhan udara, kalkulator ini membantu dalam pengelolaan biaya operasional dan penggunaan sumber daya yang lebih baik.

    4. Peningkatan Kinerja Peralatan: Proses pembakaran yang optimal dapat memperpanjang umur peralatan dan mengurangi kebutuhan perawatan, sehingga mengurangi downtime dan biaya perawatan.

    5. Pengendalian Proses: Dengan memastikan proses pembakaran berjalan sesuai dengan spesifikasi yang diinginkan, kalkulator ini membantu dalam menjaga konsistensi dan kualitas proses produksi.
    """)

     # Daftar Anggota Kelompok
    st.subheader("Anggota Kelompok")
    
    anggota_kelompok = [
        "1. Adzikri Ilham Trinanda (2330480)",
        "2. Alya lu'luil Maknun (2330485)",
        "3. Fathoni Atri Dynabaar (2330502)",
        "4. M. Edho Romadhona (2118919)",
        "5. Nabila Rahmayanti Nurjanah (2330516)",
        "6. Qonita Hafizah (2330521)"
    ]
    
    st.write("\n".join(anggota_kelompok))

with tab2:

# Judul Utama
    st.header("Perhitungan Kebutuhan Oksigen dan Udara untuk Pembakaran Batubara")
    st.header('', divider='rainbow')


# Subheader dan Deskripsi
    st.subheader("Menghitung Kebutuhan Oksigen")
    st.write("Menentukan jumlah oksigen yang diperlukan berdasarkan komposisi batubara dan kondisi pembakaran.")

    st.subheader("Menghitung Udara Stoikiometri")
    st.write("Menghitung jumlah udara ideal (tanpa berlebih) yang diperlukan untuk pembakaran lengkap batubara.")

    st.subheader("Menghitung Udara Berlebih")
    st.write("Menghitung berapa banyak udara tambahan yang dibutuhkan di atas udara stoikiometri untuk memastikan pembakaran yang efisien dan mencegah pembakaran tidak lengkap.")

    st.subheader("Menghitung Udara Aktual")
    st.write("Menghitung total jumlah udara yang diperlukan dengan mempertimbangkan udara berlebih dan komposisi udara (oksigen dan nitrogen).")

# Input yang Diperlukan
    st.subheader("Input yang Diperlukan")
    st.write("""
    - Massa Batubara: Berat batubara yang terbakar dalam satuan kilogram per jam.
    - Kandungan Karbon: Persentase karbon dalam batubara.
    - Kandungan Hidrogen: Persentase hidrogen dalam batubara.
    - Kandungan Nitrogen: Persentase nitrogen dalam batubara.
    - Kandungan Oksigen: Persentase oksigen dalam batubara.
    - Kandungan Sulfur: Persentase sulfur dalam batubara.
    - Kandungan Air: Persentase kelembaban dalam batubara.
    - Kandungan Abu: Persentase abu dalam batubara.
    - Udara Berlebih: Persentase udara tambahan yang diinginkan untuk pembakaran.
    """)

# Proses Perhitungan
    st.subheader("Proses Perhitungan")
    st.write("""
    1. Menghitung Massa Komponen: Menghitung massa setiap komponen batubara berdasarkan persentase komposisi.
    2. Menghitung Laju Alir Mol: Menghitung laju alir mol untuk masing-masing komponen (karbon, hidrogen, sulfur, nitrogen, dan oksigen) berdasarkan massa komponen.
    3. Menghitung Total Oksigen yang Dibutuhkan: Menjumlahkan laju alir mol oksigen yang diperlukan untuk setiap komponen batubara.
    4. Menghitung Udara Stoikiometri: Menghitung jumlah udara yang ideal (stoikiometri) berdasarkan kebutuhan oksigen.
    5. Menghitung Udara Berlebih: Menambahkan persentase udara berlebih untuk memastikan pembakaran yang efisien.
    6. Menghitung Udara Aktual: Menghitung total udara yang diperlukan dengan udara berlebih, dan menentukan massa oksigen dan nitrogen yang diperlukan.
    """)

# Output yang Dihasilkan
    st.subheader("Output yang Dihasilkan")
    st.write("""
    - Jumlah Oksigen yang Dibutuhkan (kmol/jam): Total jumlah oksigen yang diperlukan untuk pembakaran.
    - Udara Stoikiometri (kmol/jam): Jumlah udara ideal yang diperlukan untuk pembakaran.
    - Udara Berlebih (%): Persentase udara tambahan yang digunakan.
    - Udara Aktual (kmol/jam): Jumlah udara total yang diperlukan, termasuk udara berlebih.
    - Massa Oksigen (kg/jam): Massa oksigen yang diperlukan.
    - Massa Nitrogen (kg/jam): Massa nitrogen yang diperlukan.
    - Total Udara Aktual (kg/jam): Massa total udara aktual yang diperlukan.
    """)


with tab3:
    st.header("Silahkan INPUT data anda pada SIDE-BAR")
    st.header('', divider='rainbow')
    # Sidebar hanya ditampilkan di tab ini
    st.sidebar.title("Masukkan Data Massa Elemen")

    # Input dari pengguna
    kg_batubara = st.sidebar.number_input("Berapa Kg Batu bara yang terbakar dalam 1 jam ? (Kg)", value=70000.0)
    karbon_butuh = st.sidebar.number_input("Masukkan kandungan karbon (%)", min_value=0.0, max_value=100.0, value=43.05)
    hidrogen_butuh = st.sidebar.number_input("Masukkan kandungan hidrogen (%)", min_value=0.0, max_value=100.0, value=3.27)
    nitrogen_butuh = st.sidebar.number_input('Masukan kandungan nitrogen (%)', min_value=0.0, max_value=100.0, value=0.57)
    oxigen_butuh = st.sidebar.number_input("Masukkan kandungan oksigen (%)", min_value=0.0, max_value=100.0, value=14.11)
    sulfur_butuh = st.sidebar.number_input("Masukkan kandungan sulfur (%)", min_value=0.0, max_value=100.0, value=0.12)
    air_butuh = st.sidebar.number_input("Masukkan kandungan kelembaban (%)", min_value=0.0, max_value=100.0, value=35.08)
    abu_butuh = st.sidebar.number_input("Masukkan kandungan abu (%)", min_value=0.0, max_value=100.0, value=3.8)
    udara_lebih = st.sidebar.number_input("Masukkan udara berlebih yang ingin digunakan (%)", min_value=0.0, max_value=100.0, value=20.0)

    # Tombol untuk menghitung
    if st.button("Hitung Oksigen yang Dibutuhkan"):
        # LAJU ALIR MASSA
        massa_karbon = (karbon_butuh / 100) * kg_batubara
        massa_hidrogen = (hidrogen_butuh / 100) * kg_batubara
        massa_sulfur = (sulfur_butuh / 100) * kg_batubara
        massa_nitrogen = (nitrogen_butuh / 100) * kg_batubara
        massa_oxigen = (oxigen_butuh / 100) * kg_batubara
        massa_air = (air_butuh / 100) * kg_batubara
        massa_abu = (abu_butuh / 100 ) * kg_batubara

        # LAJU ALIR MOL
        oxigen_for_karbon = (massa_karbon / 12 )
        oxigen_for_hidrogen = (massa_hidrogen / 4 )
        oxigen_for_sulfur = (massa_sulfur / 32 )
        oxigen_for_nitrogen = (massa_nitrogen / 14 )
        oxigen_for_oxigen = (massa_oxigen / 16 )
        oxigen_for_air = (massa_air / 18 )
        oxigen_for_abu = 0

        # kebutuhan oksigen
        mol_karbon = oxigen_for_karbon
        mol_hidrogen = oxigen_for_hidrogen
        mol_nitrogen = oxigen_for_nitrogen
        mol_sulfur = oxigen_for_sulfur
        mol_air = oxigen_for_air    
        mol_oxigen = oxigen_for_oxigen / 2
        mol_abu = oxigen_for_abu
        mol_total = mol_karbon + mol_nitrogen + mol_hidrogen + mol_sulfur - mol_oxigen

        # Kandungan udara stokiometri (o2=21% n2=79%)
        udara_stoikio = (mol_total / 21)*100

        # udara berlebih 
        udara_berlebih = udara_stoikio + (udara_stoikio * (udara_lebih / 100))

        # udara aktual
        oksigen_aktual = udara_berlebih * 0.21
        nitrogen_aktual = udara_berlebih * 0.79
        kg_oksigen = oksigen_aktual * 32
        kg_nitrogen = nitrogen_aktual * 27.99322
        udara_aktual = kg_oksigen + kg_nitrogen

        total_oxygen_needed = oxigen_for_karbon + oxigen_for_hidrogen + oxigen_for_sulfur + oxigen_for_nitrogen

        data = {
            "Komponen": ["Karbon", "Hidrogen", "Sulfur", "Nitrogen", "Oksigen", "Air", "Abu", "Total oksigen yang dibutuhkan"],
            "% Berat" : [karbon_butuh, hidrogen_butuh, sulfur_butuh, nitrogen_butuh, oxigen_butuh, air_butuh, abu_butuh, "" ],
            "Massa (kg/jam)" : [massa_karbon, massa_hidrogen, massa_sulfur, massa_nitrogen, massa_oxigen, massa_air, massa_abu,  ""],
            "Mol (kmol/jam)" : [oxigen_for_karbon, oxigen_for_hidrogen, oxigen_for_sulfur, oxigen_for_nitrogen, oxigen_for_oxigen, oxigen_for_air, oxigen_for_abu, ""],
            "Oksigen yang Dibutuhkan (kg)": [mol_karbon, mol_hidrogen , mol_sulfur, mol_nitrogen, mol_oxigen, mol_air, mol_abu, mol_total] 
        }

        df = pd.DataFrame(data)

        # Mengurangi jumlah angka di belakang koma menjadi 4
        df['Massa (kg/jam)'] = df['Massa (kg/jam)'].round(4)
        df['Mol (kmol/jam)'] = df['Mol (kmol/jam)'].round(4)
        df['Oksigen yang Dibutuhkan (kg)'] = df['Oksigen yang Dibutuhkan (kg)'].round(4)

        st.write("Hasil Perhitungan Oksigen yang Dibutuhkan:")

        # Fungsi untuk styling
        def highlight_red(val):
            color = 'red' if val != "" else 'grey'
            return 'color: %s' % color

# Terapkan styling menggunakan Styler
        styled_df = df.style.applymap(highlight_red)

# Tampilkan dataframe yang sudah distyling
        styled_df

        # Menyusun data untuk tabel
        data_rangkuman = {
            "Deskripsi": [
                "Jumlah Oksigen yang Dibutuhkan (kmol/jam)",
                "Udara Stoikiometri (kmol/jam)",
                "Udara Berlebih (%)",
                "Udara Aktual (kmol/jam)",
                "Oksigen Aktual 21% (kmol/jam)",
                "Nitrogen Aktual 79% (kmol/jam)",
                "Massa Oksigen (kg/jam)",
                "Massa Nitrogen (kg/jam)",
                "Total Udara Aktual (kg/jam)"
            ],
            "Nilai": [
                f"{mol_total:.2f}",
                f"{udara_stoikio:.2f}",
                f"{udara_lebih:.2f}",
                f"{udara_berlebih:.2f}",
                f"{oksigen_aktual:.2f}",
                f"{nitrogen_aktual:.2f}",
                f"{kg_oksigen:.2f}",
                f"{kg_nitrogen:.2f}",
                f"{udara_aktual:.2f}"
            ]
        }

        df_rangkuman = pd.DataFrame(data_rangkuman)

        st.write("Rangkuman Hasil Perhitungan:")

        # Fungsi untuk styling
        def highlight_red(val):
            color = 'red' if val != "" else 'grey'
            return 'color: %s' % color

# Terapkan styling menggunakan Styler
        styled_dr = df_rangkuman.style.applymap(highlight_red)

# Tampilkan dataframe yang sudah distyling
        styled_dr
