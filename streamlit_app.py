import streamlit as st
import pandas as pd
import datetime
import os

# ===============================
# 1. CONFIG & INITIAL STATE
# ===============================
st.set_page_config(page_title="AKA-LABBROWS", layout="wide", page_icon="🔬")

st.markdown("""
    <style>
    /* 1. Background Jingga Muda Statis */
    .stApp {
        background-color: #FFCC80; 
        color: #333333; 
    }

    /* 2. Sidebar Jingga Muda Keputihan */
    [data-testid="stSidebar"] {
        background-color: #FFF3E0 !important; 
        border-right: 1px solid #FFE0B2;
    }

    /* 3. Menyesuaikan teks di Sidebar */
    [data-testid="stSidebar"] * {
        color: #5D4037 !important; 
    }

    /* 4. Efek Kontainer/Card */
    .st-emotion-cache-1kyx9g7 {
        background: rgba(255, 255, 255, 0.4) !important; 
        backdrop-filter: blur(5px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        padding: 25px !important;
        box-shadow: 0 4px 15px 0 rgba(0, 0, 0, 0.05) !important;
    }

    /* 5. Mempercantik Tombol */
    .stButton>button {
        border-radius: 20px;
        background: #FB8C00; 
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #F57C00 !important;
        color: white !important;
        transform: scale(1.02);
    }

    /* Judul Utama */
    h1 {
        color: #E65100; 
        font-weight: 800 !important;
    }
    </style>
    """, unsafe_allow_html=True)

if "lab_terpilih" not in st.session_state:
    st.session_state.lab_terpilih = None

def reset_lab():
    st.session_state.lab_terpilih = None

# ===============================
# 2. DATABASE (Integrated with New Schedule)
# ===============================
DATABASE_LAB = {
    "Lab Organik": {
        "gedung": "Gedung D", 
        "key": "lab_org_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Gunakan APD lengkap (jas lab, sepatu tertutup, masker, dan kacamata pengaman).",
            "3. Reaksi yang melibatkan larutan pekat wajib dilakukan di dalam lemari asam.",
            "4. Pahami MSDS dan simbol bahaya bahan kimia organik sebelum memulai sintesis.",
            "5. Pembuangan limbah pelarut organik harus dipisah (halogen dan non-halogen).",
            "6. Dilarang makan, minum, atau menyimpan bahan makanan di area meja kerja lab.",
            "7. Pastikan seluruh kran gas dan air tertutup rapat sebelum meninggalkan laboratorium.",
            "8. Lapor kepada laboran jika terjadi tumpahan bahan kimia atau alat gelas pecah."
        ],
        "dosen": [{"nama": "ayung, M.Si", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["07:30 - 17:30", "", "", "12:30 - 17:30", ""],
            "Kegiatan": ["Praktik kelas 1G", "", "", "Praktik kelas 2A", ""]
        })
    },
    "Lab Analitik": {
        "gedung": "Gedung D",
        "key": "lab_ana_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Wajib menggunakan APD sesuai standar prosedur analisis kimia.",
            "3. Pastikan timbangan analitik dalam kondisi bersih dan terkalibrasi sebelum digunakan.",
            "4. Gunakan pipet volume dan alat ukur gelas dengan teknik yang benar untuk akurasi data.",
            "5. Dilarang membuang larutan asam/basa kuat langsung ke wastafel tanpa penetralan.",
            "6. Jaga kebersihan area titrasi dan meja instrumen dari ceceran larutan standar.",
            "7. Lakukan pencatatan logbook penggunaan alat dan bahan kimia secara tertib.",
            "8. Cuci seluruh peralatan gelas dengan air demineralisasi setelah digunakan."
        ],
        "dosen": [{"nama": "Pak Joko", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["", "07:30 - 17:30", "", "", "07:30 - 12:30"],
            "Kegiatan": ["", "Praktik kelas 2E1", "", "", "Praktik kelas 2F"]
        })
    },
    "Lab Lingkungan": {
        "gedung": "Gedung D",
        "key": "lab_ling_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Gunakan masker dan sarung tangan saat menangani sampel air limbah atau tanah.",
            "3. Lakukan pengolahan awal limbah berbahaya sebelum dibuang ke saluran pembuangan.",
            "4. Dilarang mencampur sampel lingkungan dengan bahan kimia tanpa label yang jelas.",
            "5. Bersihkan wadah sampel dan area kerja setelah melakukan ekstraksi.",
            "6. Simpan reagen kimia pada lemari penyimpanan yang sesuai dengan klasifikasinya.",
            "7. Laporkan segera jika terdapat kerusakan pada sistem filtrasi atau pengolahan air."
        ],
        "dosen": [{"nama": "Pak Purbay", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["07:30 - 17:30", "", "07:30 - 12:30", "12:30 - 17:30", ""],
            "Kegiatan": ["Praktik kelas 1D", "", "Praktik kelas 2F", "Praktik kelas 2A", ""]
        })
    },
    "Lab Instrumen": {
        "gedung": "Gedung E",
        "key": "lab_ins_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Dilarang menyalakan instrumen tanpa pendampingan atau izin laboran.",
            "3. Pastikan tegangan listrik stabil dan UPS berfungsi sebelum menjalankan alat.",
            "4. Gunakan larutan standar dengan kemurnian tinggi (Pro Analysis) untuk hasil maksimal.",
            "5. Dilarang membawa makanan atau minuman ke dalam ruangan instrumen ber-AC.",
            "6. Wajib mengisi logbook penggunaan instrumen secara detail (durasi dan status alat).",
            "7. Bersihkan sel cuvet atau kolom kromatografi sesuai SOP setelah prosedur selesai.",
            "8. Matikan instrumen sesuai urutan tombol power (SOP shutdown) yang benar."
        ],
        "dosen": [{"nama": "Pak DD", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["07:30 - 17:30", "", "", "12:30 - 17:30", "07:30 - 17:30"],
            "Kegiatan": ["Praktik kelas 1G", "", "", "Praktik kelas 2G", "Praktik kelas 1B"]
        })
    },
    "Lab Mikro": {
        "gedung": "Gedung E",
        "key": "lab_mikro_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Gunakan jas lab yang bersih dan lakukan sterilisasi tangan sebelum bekerja.",
            "3. Bekerja secara aseptis di dekat api bunsen atau di dalam Laminar Air Flow (LAF).",
            "4. Pastikan autoclave digunakan sesuai prosedur untuk sterilisasi media dan alat.",
            "5. Dilarang membuka cawan petri berisi biakan mikroba secara sembarangan di luar LAF.",
            "6. Buang limbah biologis (bekas biakan) ke dalam kantong kuning untuk autoklaf.",
            "7. Lapor kepada laboran jika terjadi kontaminasi atau kerusakan pada inkubator."
        ],
        "dosen": [{"nama": "Bu CC", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["", "", "07:30 - 17:30", "12:30 - 17:30", ""],
            "Kegiatan": ["", "", "Praktik kelas 1E", "Praktik kelas 2A", ""]
        })
    },
    "Lab Fisika": {
        "gedung": "Gedung F",
        "key": "lab_fisika_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Gunakan sepatu tertutup yang kering untuk menghindari risiko sengatan listrik.",
            "3. Periksa sambungan kabel dan pastikan tidak ada kabel yang terkelupas sebelum praktikum.",
            "4. Dilarang menyentuh komponen listrik dengan tangan basah atau tanpa alas kaki.",
            "5. Gunakan multimeter dan alat ukur listrik sesuai dengan rentang batas ukurnya.",
            "6. Pastikan sumber tegangan (power supply) dalam posisi 'Off' saat merangkai sirkuit.",
            "7. Rapikan kembali alat peraga, kabel penghubung, dan statif ke tempat penyimpanan.",
            "8. Lapor segera jika tercium bau terbakar atau melihat percikan api pada rangkaian."
        ],
        "dosen": [{"nama": "Mas Jaka", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["07:30 - 17:30", "07:30 - 17:30", "07:30 - 17:30", "12:30 - 17:30", ""],
            "Kegiatan": ["Praktik kelas 1G", "Praktik kelas 2C", "Praktik kelas 1D", "Praktik kelas 2A", ""]
        })
    },
    "Lab Teknologi": {
        "gedung": "Gedung G",
        "key": "lab_tek_unique",
        "regulasi": [
            "1. Wajib koordinasi dengan dosen pembimbing penelitian dan laboran penanggung jawab lab.",
            "2. Gunakan sepatu safety, masker, dan sarung tangan saat melakukan penelitian.",
            "3. Isi logbook pemakaian instrument analitik dan instrumen proses.",
            "4. Dilarang menggunakan intrumet tanpa seizin laboran teknologi.",
            "5. Pastikan kebersihan alat proses (evaporator, dryer, dll) sebelum dan sesudah running.",
            "6. Lakukan pengecekan ketersediaan gas jika diperlukan.",
            "7. Simpan hasil produk teknologi pada wadah yang aman dan berikan label identitas.",
            "8. Laporkan jika terdapat kebocoran atau suara mesin yang tidak normal."
        ],
        "dosen": [{"nama": "agoy, M.Si", "telp": "08xxx"}],
        "link_form": "https://forms.gle/GtHJswG8noyFvoHW7",
        "data_jadwal": pd.DataFrame({
            "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
            "Jam": ["", "07:30 - 17:30", "", "07:30 - 17:30", ""],
            "Kegiatan": ["", "Praktik kelas 1G", "", "Praktik kelas 2C", ""]
        })
    }
}

# ===============================
# 3. FUNGSI TAMPILAN
# ===============================
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
        st.link_button("📑 Formulir Peminjaman Eksternal", data["link_form"], type="primary", use_container_width=True)
    with col2:
        st.subheader("👨‍🔬 Dosen & Laboran")
        for d in data["dosen"]:
            with st.container(border=True):
                st.write(f"**{d['nama']}**")
                st.caption(f"📞 {d['telp']}")

def tampilkan_gedung(nama_gedung):
    st.header(f"🏢 {nama_gedung}")
    fotos = {
        "Gedung D": "https://via.placeholder.com/800x300.png?text=GEDUNG+D",
        "Gedung E": "https://via.placeholder.com/800x300.png?text=GEDUNG+E",
        "Gedung F": "https://via.placeholder.com/800x300.png?text=GEDUNG+F",
        "Gedung G": "https://via.placeholder.com/800x300.png?text=GEDUNG+G"
    }
    st.image(fotos.get(nama_gedung, "https://via.placeholder.com/800x300"), caption=f"Area {nama_gedung}")
    st.divider()
    st.write("### Pilih Laboratorium:")
    lab_di_gedung = {k: v for k, v in DATABASE_LAB.items() if v["gedung"] == nama_gedung}
    if lab_di_gedung:
        cols = st.columns(len(lab_di_gedung))
        for i, (nama_lab, info) in enumerate(lab_di_gedung.items()):
            with cols[i]:
                if st.button(f"Informasi {nama_lab}", key=info["key"]):
                    st.session_state.lab_terpilih = nama_lab
                    st.rerun()

def lihat_jadwal():
    st.header("📅 Jadwal Laboratorium")
    lab_nama = st.selectbox(
        "Pilih Laboratorium",
        options=list(DATABASE_LAB.keys())
    )
    st.subheader(f"Tabel Jadwal {lab_nama}")
    df = DATABASE_LAB[lab_nama].get("data_jadwal")
    if df is not None:
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.warning("Data jadwal tidak tersedia.")

# ===============================
# 4. SIDEBAR & ROUTING
# ===============================
with st.sidebar:
    st.title("🔬 Lab-Info System")
    st.write("---")
    menu = st.radio(
        "Navigasi Utama", 
        ["Beranda", "Jadwal Lab", "Gedung D", "Gedung E", "Gedung F", "Gedung G"], 
        on_change=reset_lab
    )

if st.session_state.lab_terpilih:
    halaman_detail_lab(st.session_state.lab_terpilih)
else:
    if menu == "Beranda":
        st.title("Welcome To AKA-LABBROWS")
        st.write("**Projek Logika Dan Pemrograman Komputer - Kelompok 4**")
        st.write("Tempat khusus untuk kamu yang ingin meminjam lab di Politeknik AKA Bogor.")
        st.video("https://youtu.be/F-j-BGyRNKo")
        st.write("Politeknik AKA Bogor didirikan pada tahun 1959 dan merupakan perguruan tinggi di lingkungan Kementerian Perindustrian. Terdapat beberapa laboratorium yang terdapat di Politeknik AKA Bogor, antara lain, Gedung D (Lab Organik, Lab Analitik, Lab Lingkungan), Gedung E (Lab Instrumen, Lab Mikro), Gedung F (Lab Fisika), Gedung G (Lab Teknologi).")
        st.balloons()
    elif menu == "Jadwal Lab":
        lihat_jadwal()
    else:
        tampilkan_gedung(menu)
