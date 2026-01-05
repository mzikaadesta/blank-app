import streamlit as st

st.set_page_config(page_title="Sistem Informasi Laboratorium", layout="wide", page_icon="🔬")

# ===============================
# DATABASE LAB (DATA ASLI DOKUMEN)
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
            "1. wwww dresscode lab lengkap",
            "2. wwww dilarang makan/minum",
            "3. wwww cek alat sebelum pakai",
            "4. wwww bersihkan meja setelah praktikum",
            "5. wwww lapor jika ada kerusakan"
        ],
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2"},
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3"},
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
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
            "1. bbbbbbbbbb",
            "2. bbbbbbbbbbb",
            "3. bbbbbbbbbbbb",
            "4. bbbbbbbbbbb",
            "5. bbbbbbbbbbbbb"
        ],
        "dosen": [
            {"nama": "Pak Joko", "telp": "Kode 5"},
            {"nama": "Bu Puan", "telp": "Kode 6"},
            {"nama": "Bu Sri", "telp": "Kode 7"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
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
            "1. pppppppppp",
            "2. ppppppppppp",
            "3. pppppppppppp",
            "4. ppppppppppp",
            "5. ppppppppppppp"
        ],
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8"},
            {"nama": "Bu Retno", "telp": "Kode 9"},
            {"nama": "Mas Jaka", "telp": "Kode 10"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
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
            "1. 0000000000",
            "2. 00000000000",
            "3. 000000000000",
            "4. 00000000000",
            "5. 0000000000000"
        ],
        "dosen": [
            {"nama": "Pak DD", "telp": "Kode 11"},
            {"nama": "Bu CC", "telp": "Kode 12"},
            {"nama": "Mas HH", "telp": "Kode 13"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
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
            "1. mmmmmmmmmm",
            "2. mmmmmmmmmmm",
            "3. mmmmmmmmmmmm",
            "4. mmmmmmmmmmm",
            "5. mmmmmmmmmmmmm"
        ],
        "dosen": [
            {"nama": "Pak Purbay", "telp": "Kode 8"},
            {"nama": "Bu Retno", "telp": "Kode 9"},
            {"nama": "Mas Jaka", "telp": "Kode 10"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
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
            "1. msmsmsmsmsmsms",
            "2. msmsmsmsmsmsmsms",
            "3. msmsmsmsmsmsmsmsms",
            "4. msmsmsmsmsmsmsms",
            "5. msmsmsmsmsmsmsmsms"
        ],
        "dosen": [
            {"nama": "Golda, M.Si", "telp": "Kode 2"},
            {"nama": "Siti Indomi, M.Si", "telp": "Kode 3"},
            {"nama": "Ultra Mikk. Amd, Si", "telp": "Kode 4"},
        ],
        "link_form": "https://youtu.be/opl6dScRQzQ"
    }
}

# ===============================
# FUNGSI NAVIGASI & TAMPILAN
# ===============================
if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

def halaman_detail_lab(nama_lab):
    data = DATABASE_LAB[nama_lab]
    st.button("⬅ Kembali ke Menu Utama", on_click=reset_lab)
    st.title(f"🔬 {nama_lab}")
    st.divider()

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("📜 Regulasi Peminjaman")
        for r in data["regulasi"]:
            st.write(r)
        st.divider()
        st.link_button("🌐 Klik Untuk Formulir Peminjaman", data["link_form"], type="primary", use_container_width=True)

    with col2:
        st.subheader("👨‍🔬 Dosen & Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    for nama_lab, info in lab_di_gedung.items():
        if st.button(f"Pilih {nama_lab}", key=info["key"]):
            st.session_state.lab_terpilih = nama_lab
            st.rerun()

def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")
    lab_nama = st.selectbox("Pilih Lab", list(DATABASE_LAB.keys()))
    hari = st.selectbox("Pilih Hari", ["senin", "selasa", "rabu", "kamis", "jumat"])
    jadwal_hari = DATABASE_LAB[lab_nama]["jadwal"].get(hari)
    if jadwal_hari:
        for jam, kls in jadwal_hari.items():
            st.info(f"🕒 **{jam}** — Kelas **{kls}**")
    else:
        st.warning("Tidak ada jadwal.")

# ===============================
# ROUTING
# ===============================
with st.sidebar:
    st.title("Menu Lab")
    menu = st.radio("Pilih Menu", ["Jadwal Lab", "Gedung B", "Gedung E", "Gedung F", "Gedung G"], on_change=reset_lab)

if st.session_state.lab_terpilih:
    halaman_detail_lab(st.session_state.lab_terpilih)
else:
    if menu == "Jadwal Lab": lihat_jadwal()
    else: tampilkan_gedung(menu)
