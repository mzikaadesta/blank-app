import streamlit as st

st.set_page_config(page_title="Sistem Laboratorium", layout="wide", page_icon="🔬")

# ===============================
# DATABASE (SIMULASI)
# ===============================
# Data digabung agar lebih mudah dikelola (Satu sumber kebenaran)
DATABASE_LAB = {
    "Lab Organik": {
        "gedung": "Gedung B",
        "key": "organik",
        "jadwal": {
            "senin": {"07.00": "1A", "10.00": "1B"},
            "selasa": {"07.00": "2A"}
        },
        "regulasi": ["Wajib memakai jas lab putih", "Dilarang membawa makanan", "Gunakan masker"],
        "dosen": [
            {"nama": "Dosen Organik 1", "telp": "08123456789", "foto": "https://via.placeholder.com/150"},
            {"nama": "Dosen Organik 2", "telp": "08123456780", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Analisis": {
        "gedung": "Gedung B",
        "key": "analisis",
        "jadwal": {
            "senin": {"07.00": "2B"},
            "selasa": {"10.00": "2C"}
        },
        "regulasi": ["Wajib sarung tangan nitrile", "Cek alat sebelum digunakan"],
        "dosen": [
            {"nama": "Dosen Analisis 1", "telp": "08123456781", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Instrument": {
        "gedung": "Gedung E",
        "key": "instrument",
        "jadwal": {
            "senin": {"07.00": "2D"},
        },
        "regulasi": ["Pastikan tegangan stabil", "Dilarang mematikan alat tanpa prosedur"],
        "dosen": [
            {"nama": "Dosen Instrument 1", "telp": "08123456782", "foto": "https://via.placeholder.com/150"},
        ]
    },
    "Lab Lingkungan": {
        "gedung": "Gedung D",
        "key": "lingkungan",
        "jadwal": {
            "selasa": {"10.00": "1C"},
        },
        "regulasi": ["Buang limbah pada tempatnya", "Cuci tangan setelah praktikum"],
        "dosen": [
            {"nama": "Dosen Lingkungan 1", "telp": "08123456783", "foto": "https://via.placeholder.com/150"},
        ]
    }
}

# ===============================
# SESSION STATE & NAVIGASI
# ===============================
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

# ===============================
# FUNGSI HALAMAN
# ===============================

def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")
    col1, col2 = st.columns(2)
    
    with col1:
        lab_nama = st.selectbox("Pilih Lab", list(DATABASE_LAB.keys()))
    with col2:
        hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])

    jadwal_data = DATABASE_LAB[lab_nama]["jadwal"].get(hari)

    if jadwal_data:
        for jam, kelas in jadwal_data.items():
            st.info(f"🕒 **{jam}** — Kelas **{kelas}**")
    else:
        st.warning(f"Tidak ada jadwal untuk {lab_nama} pada hari {hari.capitalize()}.")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    st.write(f"Daftar Laboratorium yang tersedia di {nama_gedung}:")
    
    # Filter lab berdasarkan gedung
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    
    for nama_lab, info in lab_di_gedung.items():
        if st.button(f"Masuk ke {nama_lab}", key=info["key"]):
            st.session_state.lab_terpilih = nama_lab
            st.rerun()

def halaman_detail_lab(nama_lab):
    data = DATABASE_LAB[nama_lab]
    st.button("⬅ Kembali ke Daftar Gedung", on_click=reset_lab)
    
    st.title(f"🔬 {nama_lab}")
    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📋 Regulasi & Informasi")
        for reg in data["regulasi"]:
            st.write(f"- {reg}")
        
        st.markdown("---")
        st.link_button("📄 Formulir Peminjaman Alat", "https://streamlit.io/gallery", use_container_width=True)

    with col2:
        st.subheader("👨‍🔬 Dosen / Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.image(d["foto"], width=100)
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")

# ===============================
# SIDEBAR
# ===============================
with st.sidebar:
    st.title("Menu Utama")
    # Reset lab_terpilih jika menu sidebar diklik agar tidak "nyangkut" di detail lab
    menu = st.radio(
        "Navigasi",
        ["Jadwal Lab", "Gedung B", "Gedung D", "Gedung E"],
        on_change=reset_lab
    )

# ===============================
# ROUTING UTAMA
# ===============================
if st.session_state.lab_terpilih:
    halaman_detail_lab(st.session_state.lab_terpilih)
else:
    if menu == "Jadwal Lab":
        lihat_jadwal()
    elif menu == "Gedung B":
        tampilkan_gedung("Gedung B")
    elif menu == "Gedung D":
        tampilkan_gedung("Gedung D")
    elif menu == "Gedung E":
        tampilkan_gedung("Gedung E")
