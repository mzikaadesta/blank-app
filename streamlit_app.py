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
import streamlit as st
st.image("data:image/jpeg;base64,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", caption="Sunrise by the mountains")
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
