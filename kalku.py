import streamlit as st
import pandas as pd
import numpy as np

# Menambahkan CSS untuk mengubah warna latar belakang menjadi hijau muda
st.markdown(
    """
    <style>
    .stApp {
        background-color: #CDFFAC;
        color: grey;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul aplikasi
st.title(":red[Kalkulator Perhitungan Oksigen untuk Pembakaran Batubara]")
st.header('', divider='rainbow')
st.write(f"Kalkulator Perhitungan Oksigen untuk Pembakaran Batubara adalah alat atau sistem perangkat lunak yang digunakan untuk menghitung kebutuhan oksigen yang diperlukan dalam proses pembakaran batubara.")
st.subheader(f"Tujuan:")
st.write(f"Memberikan estimasi atau hasil perhitungan yang akurat terkait dengan kebutuhan oksigen dalam proses pembakaran batubara. Ini membantu dalam perencanaan dan pengelolaan proses pembakaran secara efisien dan ekonomis.")

#sidebar
st.sidebar.title("Masukkan Data Massa Elemen")

# Input dari pengguna
kg_batubara = st.sidebar.number_input("Berapa Kg Batu bara yang terbakar dalam 1 jam ? (Kg)", value=70000.0)
karbon_butuh = st.sidebar.number_input("Masukkan kandungan karbon (%)", min_value=0.0, max_value=kg_batubara, value=43.05)
hidrogen_butuh = st.sidebar.number_input("Masukkan kandungan hidrogen (%)", min_value=0.0, max_value=kg_batubara, value=3.27)
nitrogen_butuh = st.sidebar.number_input('Masukan kandungan nitrogen (%)', min_value=0.0, max_value=kg_batubara, value=0.57)
oxigen_butuh = st.sidebar.number_input("Masukkan kandungan oksigen (%)", min_value=0.0, max_value=kg_batubara, value=14.11)
sulfur_butuh = st.sidebar.number_input("Masukkan kandungan sulfur (%)", min_value=0.0, max_value=kg_batubara, value=0.12)
air_butuh = st.sidebar.number_input("Masukkan kandungan kelembaban (%)", min_value=0.0, max_value=kg_batubara, value=35.08)
abu_butuh = st.sidebar.number_input("Masukkan kandungan abu (%)", min_value=0.0, max_value=kg_batubara, value=3.8)
udara_lebih = st.sidebar.number_input("Masukkan udara berlebih yang ingin digunakan (%)", min_value=0.0, max_value=100.00, value=20.0)

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
    kg_nitrogen = nitrogen_aktual * 27.9999999999
    udara_aktual = kg_oksigen + kg_nitrogen

    total_oxygen_needed = oxigen_for_karbon + oxigen_for_hidrogen + oxigen_for_sulfur + oxigen_for_nitrogen

data_komposisi_udara = {
        "Komposisi Udara": ["Oksigen", "Nitrogen"],
        "Persen komposisi (%)" : ["21", "79"],       
        "Volume Udara (kmol/jam)" : [oksigen_aktual, nitrogen_aktual],
        "Massa Aktual Udara (kg/jam)" : [kg_oksigen, kg_nitrogen ]
        }

de = pd.DataFrame(data_komposisi_udara)

data = {
        "Komponen": ["Karbon", "Hidrogen", "Sulfur", "Nitrogen", "Oksigen", "Air", "Abu", "Total oksigen yang dibutuhkan"],
        "% Berat" : [karbon_butuh, hidrogen_butuh, sulfur_butuh, nitrogen_butuh, oxigen_butuh, air_butuh, abu_butuh, "" ],
        "Massa (kg/jam)": [massa_karbon, massa_hidrogen, massa_sulfur, massa_nitrogen, massa_oxigen, massa_air, massa_abu,  ""],
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

    
st.write(f"Jumlah mol oksigen yang dibutuhkan untuk pembakaran adalah :blue-background[{mol_total:.2f}] kmol/jam oksigen.")
st.write(f"Dari jumlah mol oksigen tersebut, menghasilkan udara stoikiometri sebesar :violet-background[{udara_stoikio:.2f}] kmol/jam.")
st.write(f"Dari udara stoikiometri tersebut, digunakan udara berlebih sebesar :blue-background[{udara_lebih:.2f}%], menjadi :red-background[{udara_berlebih:.2f}] kmol/jam.")
st.write(f"Massa Oksigen dan Nitrogen dari udara berlebih sebesar :violet-background[{udara_lebih:.2f}%], Dengan asumsi komposisi udara sebagai berikut :")

# Fungsi untuk styling
def highlight_red(val):
    color = 'red' if val != "" else 'grey'
    return 'color: %s' % color

# Terapkan styling menggunakan Styler
styled_de = de.style.applymap(highlight_red)

# Tampilkan dataframe yang sudah distyling
styled_de

st.write(f"maka didapat total Udara Aktual sebesar :blue-background[{udara_aktual:.2f}] kg untuk 1 jam pembakaran Batubara seberat :red-background[{kg_batubara:.2f}] kg.")

