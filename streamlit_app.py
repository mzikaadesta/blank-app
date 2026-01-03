import streamlit as st

st.set_page_config(page_title="Sistem Laboratorium", layout="wide")

# ===============================
# DATABASE JADWAL LAB (JADWAL KELAS)
# ===============================
jadwal = {
    "Lab.organik": {
        "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
        "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
        "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
        "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
        "jumat": {"07.00": "1B", "10.00": "2D"},
    },

    "Lab.analisis": {
        "senin": {"07.00": "2A", "10.00": "2B", "14.00": "2C"},
        "selasa": {"07.00": "2D", "10.00": "2E", "14.00": "2F"},
        "rabu": {"07.00": "1A", "10.00": "1B"},
    },

    "Lab.instrument": {
        "senin": {"07.00": "2E", "10.00": "2F"},
        "selasa": {"07.00": "1G"},
    },

    "Lab.lingkungan": {
        "senin": {"07.00": "3A"},
    }
}

# ===============================
# DATABASE LAB & LABORAN
# ===============================
lab_info = {
    "Lab.organik": {
        "laboran": [
            {"nama": "Ahmad Golda, M.Si", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Siti Indomi, M.Si", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Ultra Mikk, A.Md.Si", "telp": "08vvvvvvvvvvvvv"},
        ]
    },
    "Lab.analisis": {
        "laboran": [
            {"nama": "Pak Joko", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Bu Puan", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Bu Sri", "telp": "08vvvvvvvvvvvvv"},
        ]
    },
    "Lab.instrument": {
        "laboran": [
            {"nama": "Pak DD", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Bu CC", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Mas HH", "telp": "08vvvvvvvvvvvvv"},
        ]
    },
    "Lab.lingkungan": {
        "laboran": [
            {"nama": "Pak AA", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Bu BB", "telp": "08vvvvvvvvvvvvv"},
            {"nama": "Mas CC", "telp": "08vvvvvvvvvvvvv"},
        ]
    }
}

# ===============================
# SESSION STATE
# ===============================
if "hal_lab" not in st.session_state:
    st.session_state.hal_lab = "menu"
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

# ===============================
# FITUR LIHAT JADWAL
# ===============================
def lihat_jadwal():
    st.header("📅 Jadwal Penggunaan Laboratorium")

    lab = st.selectbox("Pilih Laboratorium", list(jadwal.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    data = jadwal[lab].get(hari)

    if data:
        st.subheader(f"{lab} — {hari.capitalize()}")
        for jam, kelas in data.items():
            st.write(f"🕒 {jam} → Kelas {kelas}")
    else:
        st.info("Tidak ada jadwal pada hari ini")

# ===============================
# MENU LAB
# ===============================
def menu_lab():
    st.header("🏫 Informasi Laboratorium")
    st.write("Pilih laboratorium untuk melihat detail informasi")

    for lab in lab_info.keys():
        if st.button(lab):
            st.session_state.lab_terpilih = lab
            st.session_state.hal_lab = "detail"

def detail_lab():
    lab = st.session_state.lab_terpilih
    info = lab_info[lab]

    st.header(f"🔬 {lab}")

    st.subheader("📋 Prosedur Peminjaman Lab")
    st.write("""
    1. Mengisi formulir peminjaman
    2. Menunggu persetujuan laboran
    3. Menggunakan lab sesuai jadwal
    4. Membersihkan dan mengembalikan alat
    """)

    st.link_button(
        "📄 Formulir Peminjaman",
        "https://docs.google.com"
    )

    st.subheader("👨‍🔬 Laboran / PJ Lab")
    for l in info["laboran"]:
        st.write(f"• **{l['nama']}**")
        st.write(f"  📞 {l['telp']}")

    st.subheader("⚠️ Aturan Penggunaan")
    st.write("""
    - Wajib menggunakan APD
    - Dilarang membawa makanan/minuman
    - Bertanggung jawab terhadap alat
    """)

    if st.button("⬅ Kembali"):
        st.session_state.hal_lab = "menu"

# ===============================
# SIDEBAR MENU
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

elif menu == "Informasi Lab":
    if st.session_state.hal_lab == "menu":
        menu_lab()
    else:
        detail_lab()
