import streamlit as st

st.set_page_config(page_title="Sistem Informasi Laboratorium", layout="wide", page_icon="🔬")

# ===============================
# DATABASE LAB (BERDASARKAN DOKUMEN)
# ===============================
DATABASE_LAB = {
    "Lab Organik": {
        "gedung": "Gedung B",
        "key": "organik",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2", "foto": "https://via.placeholder.com/150"},
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3", "foto": "https://via.placeholder.com/150"},
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Analisis": {
        "gedung": "Gedung B",
        "key": "analisis",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Pak Joko", "telp": "Kode 5", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu Puan", "telp": "Kode 6", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu Sri", "telp": "Kode 7", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Lingkungan": {
        "gedung": "Gedung B",
        "key": "lingkungan",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu Retno", "telp": "Kode 9", "foto": "https://via.placeholder.com/150"},
            {"nama": "Mas Jaka", "telp": "Kode 10", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Instrumen": {
        "gedung": "Gedung E",
        "key": "instrumen",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Pak DD", "telp": "Kode 11", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu CC", "telp": "Kode 12", "foto": "https://via.placeholder.com/150"},
            {"nama": "Mas HH", "telp": "Kode 13", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Komputer": {
        "gedung": "Gedung E",
        "key": "komputer",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Pak DD", "telp": "Kode 11", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu CC", "telp": "Kode 12", "foto": "https://via.placeholder.com/150"},
            {"nama": "Mas HH", "telp": "Kode 13", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Fisika": {
        "gedung": "Gedung F",
        "key": "fisika",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8", "foto": "https://via.placeholder.com/150"},
            {"nama": "Bu Retno", "telp": "Kode 9", "foto": "https://via.placeholder.com/150"},
            {"nama": "Mas Jaka", "telp": "Kode 10", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Teknologi": {
        "gedung": "Gedung G",
        "key": "teknologi",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B", "14.00": "2A"},
            "selasa": {"07.00": "2E", "10.00": "3A", "14.00": "1C"},
            "rabu": {"07.00": "2G", "10.00": "2E", "14.00": "1G"},
            "kamis": {"07.00": "1D", "10.00": "1F", "14.00": "1A"},
            "jumat": {"07.00": "1B", "10.00": "2D"}
        },
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2", "foto": "https://via.placeholder.com/150"},
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3", "foto": "https://via.placeholder.com/150"},
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4", "foto": "https://via.placeholder.com/150"},
        ]
    }
}

# ===============================
# LOGIKA NAVIGASI
# ===============================
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

# ===============================
# FUNGSI TAMPILAN
# ===============================
def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium Lengkap")
    lab_nama = st.selectbox("Pilih Lab", list(DATABASE_LAB.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])
    
    jadwal_data = DATABASE_LAB[lab_nama]["jadwal"].get(hari)
    if jadwal_data:
        for jam, kelas in jadwal_data.items():
            st.info(f"🕒 Jam **{jam}** — Kelas **{kelas}**")
    else:
        st.warning("Tidak ada jadwal pada hari ini.")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    st.write("Silakan pilih laboratorium:")
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    
    for nama_lab, info in lab_di_gedung.items():
        if st.button(f"Lihat Detail {nama_lab}"):
            st.session_state.lab_terpilih = nama_lab
            st.rerun()

def halaman_detail_lab(nama_lab):
    data = DATABASE_LAB[nama_lab]
    st.button("⬅ Kembali", on_click=reset_lab)
    st.title(f"🔬 {nama_lab}")
    st.divider()

    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("👨‍🔬 Tim Dosen & Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")
    
    with col2:
        st.subheader("📄 Administrasi")
        st.link_button("Formulir Peminjaman Lab", "https://streamlit.io/gallery")

# ===============================
# SIDEBAR & ROUTING
# ===============================
with st.sidebar:
    st.title("Sistem Lab")
    menu = st.radio("Navigasi", ["Jadwal Lab", "Gedung B", "Gedung E", "Gedung F", "Gedung G"], on_change=reset_lab)

if st.session_state.lab_terpilih:
    halaman_detail_lab(st.session_state.lab_terpilih)
else:
    if menu == "Jadwal Lab": lihat_jadwal()
    elif menu == "Gedung B": tampilkan_gedung("Gedung B")
    elif menu == "Gedung E": tampilkan_gedung("Gedung E")
    elif menu == "Gedung F": tampilkan_gedung("Gedung F")
    elif menu == "Gedung G": tampilkan_gedung("Gedung G")
