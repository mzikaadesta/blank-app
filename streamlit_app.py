import streamlit as st

st.set_page_config(page_title="Sistem Informasi Laboratorium", layout="wide", page_icon="🔬")

# ===============================
# DATABASE LAB (DIPERBARUI DENGAN REGULASI & LINK)
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
        "regulasi": [
            "1. wwww dresscode lab lengkap", [cite: 2]
            "2. wwww dilarang makan/minum", [cite: 2]
            "3. wwww cek alat sebelum pakai", [cite: 2]
            "4. wwww bersihkan meja setelah praktikum", [cite: 2]
            "5. wwww lapor jika ada kerusakan" [cite: 2]
        ],
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4", "foto": "https://via.placeholder.com/150"}, [cite: 2]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 2]
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
        "regulasi": [
            "1. bbbbbbbbbb", [cite: 2]
            "2. bbbbbbbbbbb", [cite: 2]
            "3. bbbbbbbbbbbb", [cite: 2]
            "4. bbbbbbbbbbb", [cite: 2]
            "5. bbbbbbbbbbbbb" [cite: 2]
        ],
        "dosen": [
            {"nama": "Pak Joko", "telp": "Kode 5", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Bu Puan", "telp": "Kode 6", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Bu Sri", "telp": "Kode 7", "foto": "https://via.placeholder.com/150"}, [cite: 2]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 2]
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
        "regulasi": [
            "1. pppppppppp", [cite: 2]
            "2. ppppppppppp", [cite: 2]
            "3. pppppppppppp", [cite: 2]
            "4. ppppppppppp", [cite: 2]
            "5. ppppppppppppp" [cite: 2]
        ],
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Bu Retno", "telp": "Kode 9", "foto": "https://via.placeholder.com/150"}, [cite: 2]
            {"nama": "Mas Jaka", "telp": "Kode 10", "foto": "https://via.placeholder.com/150"}, [cite: 2]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 2]
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
        "regulasi": [
            "1. ooooooooooo", [cite: 29]
            "2. ooooooooooo", [cite: 30]
            "3. oooooooooooo", [cite: 31]
            "4. ooooooooooo", [cite: 32]
            "5. ooooooooooooo" [cite: 34]
        ],
        "dosen": [
            {"nama": "Pak DD", "telp": "Kode 11", "foto": "https://via.placeholder.com/150"}, [cite: 25]
            {"nama": "Bu CC", "telp": "Kode 12", "foto": "https://via.placeholder.com/150"}, [cite: 26]
            {"nama": "Mas HH", "telp": "Kode 13", "foto": "https://via.placeholder.com/150"}, [cite: 27]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 35]
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
        "regulasi": [
            "1. mmmmmmmmmm", [cite: 87]
            "2. mmmmmmmmmmm", [cite: 88]
            "3. mmmmmmmmmmmm", [cite: 89]
            "4. mmmmmmmmmmm", [cite: 90]
            "5. mmmmmmmmmmmmm" [cite: 91]
        ],
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8", "foto": "https://via.placeholder.com/150"}, [cite: 83]
            {"nama": "Bu Retno", "telp": "Kode 9", "foto": "https://via.placeholder.com/150"}, [cite: 84]
            {"nama": "Mas Jaka", "telp": "Kode 10", "foto": "https://via.placeholder.com/150"}, [cite: 85]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 92]
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
        "regulasi": [
            "1. msmsmsmsmsmsms", [cite: 120]
            "2. msmsmsmsmsmsms", [cite: 121]
            "3. msmsmsmsmsmsms", [cite: 122]
            "4. msmsmsmsmsmsms", [cite: 123]
            "5. msmsmsmsmsmsms" [cite: 124]
        ],
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2", "foto": "https://via.placeholder.com/150"}, [cite: 116]
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3", "foto": "https://via.placeholder.com/150"}, [cite: 117]
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4", "foto": "https://via.placeholder.com/150"}, [cite: 118]
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ" [cite: 125]
    }
}

# ===============================
# LOGIKA UTAMA & NAVIGASI
# ===============================
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

def halaman_detail_lab(nama_lab):
    data = DATABASE_LAB[nama_lab]
    st.button("⬅ Kembali ke Daftar Gedung", on_click=reset_lab)
    
    st.title(f"🔬 {nama_lab}")
    st.divider()

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.subheader("📜 Regulasi Peminjaman")
        for reg in data["regulasi"]:
            st.write(reg)
        
        st.markdown("---")
        st.subheader("📑 Formulir & Dokumen")
        st.link_button("Klik untuk Formulir Peminjaman (G-Drive)", data["link_form"], type="primary", use_container_width=True)

    with col2:
        st.subheader("👨‍🔬 Tim Dosen / Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.image(d["foto"], width=80)
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    
    cols = st.columns(len(lab_di_gedung) if lab_di_gedung else 1)
    for idx, (nama_lab, info) in enumerate(lab_di_gedung.items()):
        with cols[idx]:
            if st.button(f"Masuk {nama_lab}", key=info["key"]):
                st.session_state.lab_terpilih = nama_lab
                st.rerun()

def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")
    lab_nama = st.selectbox("Pilih Lab", list(DATABASE_LAB.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])
    
    jadwal_data = DATABASE_LAB[lab_nama]["jadwal"].get(hari)
    if jadwal_data:
        for jam, kelas in jadwal_data.items():
            st.info(f"🕒 **{jam}** — Kelas **{kelas}**")
    else:
        st.warning("Tidak ada jadwal.")

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
    else: tampilkan_gedung(menu)
