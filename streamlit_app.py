import streamlit as st

# ===============================
# DATA GEDUNG & LAB
# ===============================
gedung_lab = {
    "Lab.Ged D": ["Lab Organik", "Lab Lingkungan", "Lab Analisis"],
    "Lab.Ged E": ["Lab Instrument", "Lab Mikro", "Lab Bahasa", "Lab Komputer"],
    "Lab.Ged G": ["Lab Nanomaterial dan Teknologi"],
    "Lab.Ged F": ["Lab Fisika"]
}

# ===============================
# DATA DOSEN / LABORAN (DUMMY)
# ===============================
laboran = {
    "Lab Organik": [
        {"nama": "Laboran Organik", "telp": "08xxxx", "foto": "https://via.placeholder.com/200"}
    ],
    "Lab Lingkungan": [
        {"nama": "Laboran Lingkungan", "telp": "08xxxx", "foto": "https://via.placeholder.com/200"}
    ],
    "Lab Analisis": [
        {"nama": "Laboran Analisis", "telp": "08xxxx", "foto": "https://via.placeholder.com/200"}
    ],
    "Lab Instrument": [
        {"nama": "Laboran Instrument", "telp": "08xxxx", "foto": "https://via.placeholder.com/200"}
    ],
}

# ===============================
# SESSION STATE
# ===============================
if "page" not in st.session_state:
    st.session_state.page = "gedung"
if "gedung" not in st.session_state:
    st.session_state.gedung = None
if "lab" not in st.session_state:
    st.session_state.lab = None

# ===============================
# HALAMAN GEDUNG
# ===============================
def halaman_gedung():
    st.header("🏢 Gedung Laboratorium")
    for g in gedung_lab:
        if st.button(g):
            st.session_state.gedung = g
            st.session_state.page = "lab"

# ===============================
# HALAMAN LAB
# ===============================
def halaman_lab():
    st.header(st.session_state.gedung)
    for lab in gedung_lab[st.session_state.gedung]:
        if st.button(lab):
            st.session_state.page = lab

    if st.button("⬅ Kembali"):
        st.session_state.page = "gedung"

# ===============================
# HALAMAN LAB ORGANIK
# ===============================
def lab_organik():
    st.header("Lab Organik")

    st.subheader("📜 Regulasi")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.subheader("📄 Alur Peminjaman")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampil_laboran("Lab Organik")

# ===============================
# HALAMAN LAB LINGKUNGAN
# ===============================
def lab_lingkungan():
    st.header("Lab Lingkungan")

    st.subheader("📜 Regulasi")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.subheader("📄 Alur Peminjaman")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampil_laboran("Lab Lingkungan")

# ===============================
# HALAMAN LAB ANALISIS
# ===============================
def lab_analisis():
    st.header("Lab Analisis")

    st.subheader("📜 Regulasi")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.subheader("📄 Alur Peminjaman")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampil_laboran("Lab Analisis")

# ===============================
# HALAMAN LAB INSTRUMENT
# ===============================
def lab_instrument():
    st.header("Lab Instrument")

    st.subheader("📜 Regulasi")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.subheader("📄 Alur Peminjaman")
    st.write("1. kekekekeke\n2. kekekkekeke")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    tampil_laboran("Lab Instrument")

# ===============================
# TEMPLATE TAMPIL DOSEN
# ===============================
def tampil_laboran(nama_lab):
    st.subheader("👨‍🏫 Dosen / Laboran")
    for d in laboran.get(nama_lab, []):
        st.image(d["foto"], caption=d["nama"])
        st.write("📞", d["telp"])

    if st.button("⬅ Kembali ke Daftar Lab"):
        st.session_state.page = "lab"

# ===============================
# ROUTING
# ===============================
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
