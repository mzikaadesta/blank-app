import streamlit as st

st.set_page_config(page_title="Sistem Laboratorium", layout="wide")

# ===============================
# DATABASE JADWAL LAB (SIMULASI)
# ===============================
jadwal = {
    "Lab.organik": {
        "senin":  {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
        "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
    },
    "Lab.analisis": {
        "senin":  {"07.00": "2A", "10.00": "2B", "14.00": "2C"},
        "selasa": {"07.00": "1A", "10.00": "2D"},
    },
    "Lab.instrument": {
        "senin":  {"07.00": "2D", "10.00": "2E"},
        "selasa": {"07.00": "2F", "10.00": "2G"},
    },
    "Lab.lingkungan": {
        "senin":  {"07.00": "1A", "10.00": "2A"},
        "selasa": {"07.00": "2C", "10.00": "2D"},
    },
}

# ===============================
# DATA DOSEN / LABORAN PER LAB
# ===============================
laboran = {
    "organik": [
        {"nama": "Dosen Organik 1", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Organik 2", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Organik 3", "telp": "08vvvvvvvvvvvvv"},
    ],
    "analisis": [
        {"nama": "Dosen Analisis 1", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Analisis 2", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Analisis 3", "telp": "08vvvvvvvvvvvvv"},
    ],
    "instrument": [
        {"nama": "Dosen Instrumen 1", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Instrumen 2", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Instrumen 3", "telp": "08vvvvvvvvvvvvv"},
    ],
    "lingkungan": [
        {"nama": "Dosen Lingkungan 1", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Lingkungan 2", "telp": "08vvvvvvvvvvvvv"},
        {"nama": "Dosen Lingkungan 3", "telp": "08vvvvvvvvvvvvv"},
    ],
}

# ===============================
# SESSION STATE
# ===============================
if "lab_aktif" not in st.session_state:
    st.session_state.lab_aktif = None

# ===============================
# HALAMAN JADWAL
# ===============================
def lihat_jadwal():
    st.header("📅 Jadwal Penggunaan Laboratorium")

    lab = st.selectbox("Pilih Laboratorium", list(jadwal.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa"])

    data = jadwal[lab].get(hari)

    if data:
        st.subheader(f"{lab} — {hari.capitalize()}")
        for jam, kelas in data.items():
            st.write(f"🕒 **{jam}** → Kelas **{kelas}**")
    else:
        st.info("Tidak ada jadwal")

# ===============================
# MENU LAB
# ===============================
def menu_lab():
    st.header("🏫 Informasi Laboratorium")
    st.write("Pilih laboratorium untuk melihat regulasi, alur, dan dosen laboran")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Lab Organik"):
            st.session_state.lab_aktif = "organik"
        if st.button("Lab Analisis"):
            st.session_state.lab_aktif = "analisis"

    with col2:
        if st.button("Lab Instrument"):
            st.session_state.lab_aktif = "instrument"
        if st.button("Lab Lingkungan"):
            st.session_state.lab_aktif = "lingkungan"

# ===============================
# HALAMAN LAB ORGANIK
# ===============================
def lab_organik():
    st.header("🔬 Lab Organik")

    st.subheader("📋 Regulasi & Alur")
    st.write("• OOOOOOO")
    st.write("• OOOOOOO")
    st.write("• OOOOOOO")

    st.subheader("👨‍🔬 Dosen / Laboran")
    for d in laboran["organik"]:
        st.write(f"- **{d['nama']}** | 📞 {d['telp']}")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    if st.button("⬅ Kembali"):
        st.session_state.lab_aktif = None

# ===============================
# HALAMAN LAB LINGKUNGAN
# ===============================
def lab_lingkungan():
    st.header("🌱 Lab Lingkungan")

    st.subheader("📋 Regulasi & Alur")
    st.write("• WWWWWW")
    st.write("• WWWWWWW")
    st.write("• WWWWWW")

    st.subheader("👨‍🔬 Dosen / Laboran")
    for d in laboran["lingkungan"]:
        st.write(f"- **{d['nama']}** | 📞 {d['telp']}")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    if st.button("⬅ Kembali"):
        st.session_state.lab_aktif = None

# ===============================
# HALAMAN LAB ANALISIS
# ===============================
def lab_analisis():
    st.header("⚗️ Lab Analisis")

    st.subheader("📋 Regulasi & Alur")
    st.write("• AAAAA")
    st.write("• AAAAA")
    st.write("• AAAAA")

    st.subheader("👨‍🔬 Dosen / Laboran")
    for d in laboran["analisis"]:
        st.write(f"- **{d['nama']}** | 📞 {d['telp']}")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    if st.button("⬅ Kembali"):
        st.session_state.lab_aktif = None

# ===============================
# HALAMAN LAB INSTRUMENT
# ===============================
def lab_instrument():
    st.header("🧪 Lab Instrument")

    st.subheader("📋 Regulasi & Alur")
    st.write("• EEEEE")
    st.write("• EEEEE")
    st.write("• EEEEE")

    st.subheader("👨‍🔬 Dosen / Laboran")
    for d in laboran["instrument"]:
        st.write(f"- **{d['nama']}** | 📞 {d['telp']}")

    st.link_button("Formulir Peminjaman", "https://streamlit.io/gallery")

    if st.button("⬅ Kembali"):
        st.session_state.lab_aktif = None

# ===============================
# SIDEBAR
# ===============================
menu = st.sidebar.radio(
    "Menu",
    ["Lihat Jadwal Lab", "Informasi Lab"]
)

# ===============================
# ROUTING
# ===============================
if menu == "Lihat Jadwal Lab":
    lihat_jadwal()
else:
    if st.session_state.lab_aktif is None:
        menu_lab()
    elif st.session_state.lab_aktif == "organik":
        lab_organik()
    elif st.session_state.lab_aktif == "lingkungan":
        lab_lingkungan()
    elif st.session_state.lab_aktif == "analisis":
        lab_analisis()
    elif st.session_state.lab_aktif == "instrument":
        lab_instrument()
