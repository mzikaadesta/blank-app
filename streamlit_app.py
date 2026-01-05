import streamlit as st

# =====================================
# DATA GEDUNG & LAB
# =====================================
gedung_lab = {
    "Lab.Ged D": ["Lab Lingkungan", "Lab Organik", "Lab Analisis"],
    "Lab.Ged E": ["Lab Instrument", "Lab Mikro", "Lab Bahasa", "Lab Komputer"],
    "Lab.Ged G": ["Lab Nanomaterial dan Teknologi"],
    "Lab.Ged F": ["Lab Fisika"]
}

# =====================================
# DATA DOSEN / LABORAN
# =====================================
laboran = {
    "Lab Organik": [
        {"nama": "Pak Wowo", "telp": "08vvvv", "foto": "https://via.placeholder.com/200"},
        {"nama": "Bu Mega", "telp": "08vvvv", "foto": "https://via.placeholder.com/200"},
    ],
    "Lab Lingkungan": [
        {"nama": "Bu Sri", "telp": "08vvvv", "foto": "https://via.placeholder.com/200"},
    ],
    "Lab Analisis": [
        {"nama": "Pak Joko", "telp": "08vvvv", "foto": "https://via.placeholder.com/200"},
    ],
    "Lab Instrument": [
        {"nama": "Mas Jaka", "telp": "08vvvv", "foto": "https://via.placeholder.com/200"},
    ],
}

# =====================================
# SESSION STATE
# =====================================
if "page" not in st.session_state:
    st.session_state.page = "gedung"
if "gedung" not in st.session_state:
    st.session_state.gedung = None
if "lab" not in st.session_state:
    st.session_state.lab = None

# =====================================
# HALAMAN GEDUNG
# =====================================
def halaman_gedung():
    st.header("🏢 Gedung Laboratorium")
    for g in gedung_lab:
        if st.button(g):
            st.session_state.gedung = g
            st.session_state.page = "lab"

# =====================================
# HALAMAN LAB
# =====================================
def halaman_lab():
    st.header(st.session_state.gedung)
    for lab in gedung_lab[st.session_state.gedung]:
        if st.button(lab):
            st.session_state.lab = lab
            st.session_state.page = lab

    if st.button("⬅ Kembali"):
        st.session_state.page = "gedung"

# =====================================
# HALAMAN LAB ORGANIK
# =====================================
def lab_organik():
    st.header("🔬 Lab Organik")

    st.subheader("📜 Regulasi")
    st.write("""
    • OOOOOOO  
    • OOOOOOO  
    • OOOOOOO  
    """)

    st.subheader("📄 Alur Peminjaman")
    st.write("""
    1. OOOOOOO  
    2. OOOOOOO  
    3. OOOOOOO  
    """)

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampilkan_laboran("Lab Organik")

    tombol_kembali()

# =====================================
# HALAMAN LAB LINGKUNGAN
# =====================================
def lab_lingkungan():
    st.header("🌱 Lab Lingkungan")

    st.subheader("📜 Regulasi")
    st.write("""
    • WWWWWW  
    • WWWWWW  
    • WWWWWW  
    """)

    st.subheader("📄 Alur Peminjaman")
    st.write("""
    1. WWWWWW  
    2. WWWWWW  
    """)

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampilkan_laboran("Lab Lingkungan")

    tombol_kembali()

# =====================================
# HALAMAN LAB ANALISIS
# =====================================
def lab_analisis():
    st.header("🧪 Lab Analisis")

    st.subheader("📜 Regulasi")
    st.write("""
    • AAAAA  
    • AAAAA  
    """)

    st.subheader("📄 Alur Peminjaman")
    st.write("""
    1. AAAAA  
    2. AAAAA  
    """)

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampilkan_laboran("Lab Analisis")

    tombol_kembali()

# =====================================
# HALAMAN LAB INSTRUMENT
# =====================================
def lab_instrument():
    st.header("📡 Lab Instrument")

    st.subheader("📜 Regulasi")
    st.write("""
    • EEEEE  
    • EEEEE  
    """)

    st.subheader("📄 Alur Peminjaman")
    st.write("""
    1. EEEEE  
    2. EEEEE  
    """)

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampilkan_laboran("Lab Instrument")

    tombol_kembali()

# =====================================
# KOMPONEN BERSAMA
# =====================================
def tampilkan_laboran(lab):
    st.subheader("👨‍🏫 Dosen / Laboran")
    for d in laboran.get(lab, []):
        st.image(d["foto"], caption=d["nama"])
        st.write("📞", d["telp"])
        st.divider()

def tombol_kembali():
    if st.button("⬅ Kembali ke Daftar Lab"):
        st.session_state.page = "lab"

# =====================================
# ROUTING UTAMA
# =====================================
if st.session_state.page == "gedung":
    halaman_gedung()
elif st.session_state.page == "lab":
    halaman_lab()
elif st.session_state.page == "Lab Organik":
    lab_organik()
elif st.session_state.page == "Lab Lingkungan":
    lab_lingkungan()
elif st.session_state.page == "Lab Analisis":
    lab_analisis()
elif st.session_state.page == "Lab Instrument":
    lab_instrument()
