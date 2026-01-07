import streamlit as st
import re
import time

# =========================================================
# 1. DATA STATIS (Massa Atom & Tabel Periodik)
# =========================================================
massa_atom = {
    "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, 
    "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "Ne": 20.18,
    "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97,
    "S": 32.07, "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08,
    "Fe": 55.85, "Pb": 207.2, "Cu": 63.55, "Zn": 65.38, "Ag": 107.87
}

# Struktur sederhana Tabel Periodik (Simbol, Golongan)
elemen_periodik = [
    [{"simbol": "H", "gol": "IA"}, {"simbol": "", "gol": ""}, {"simbol": "He", "gol": "VIIIA"}],
    [{"simbol": "Li", "gol": "IA"}, {"simbol": "Be", "gol": "IIA"}, {"simbol": "B", "gol": "IIIA"}],
    [{"simbol": "Na", "gol": "IA"}, {"simbol": "Mg", "gol": "IIA"}, {"simbol": "Al", "gol": "IIIA"}]
    # Tambahkan elemen lain sesuai kebutuhan makalah
]

# =========================================================
# 2. LOGIKA REAKSI KIMIA (Reaction Engine)
# =========================================================
reaksi_database = {
    frozenset(["H", "O"]): {"setara": "2H_2 + O_2 \\rightarrow 2H_2O", "produk": "H2O"},
    frozenset(["Na", "Cl"]): {"setara": "2Na + Cl_2 \\rightarrow 2NaCl", "produk": "NaCl"},
    frozenset(["Fe", "Cl"]): {"setara_opsi": ["Fe + Cl_2 \\rightarrow FeCl_2", "2Fe + 3Cl_2 \\rightarrow 2FeCl_3"], "produk_opsi": ["FeCl2", "FeCl3"]}
}

def hitung_massa_molekul(rumus):
    pattern = r'([A-Z][a-z]?)(\d*)'
    res = re.findall(pattern, rumus)
    try:
        total = 0
        for simbol, jumlah in res:
            jumlah = int(jumlah) if jumlah else 1
            total += massa_atom.get(simbol, 0) * jumlah
        return total
    except: return None

# =========================================================
# 3. ANTARMUKA (UI & Layout)
# =========================================================
st.set_page_config(page_title="Penyusun Reaksi Kimia", layout="wide")

# CSS untuk Glassmorphism & Background (Sesuai permintaan sebelumnya)
st.markdown("""
    <style>
    .stApp { background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab); background-size: 400% 400%; animation: gradient 15s ease infinite; }
    @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    .stButton>button { border-radius: 10px; background: rgba(255,255,255,0.2); color: white; border: 1px solid white; }
    h1, h3, p { color: white !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🔬 Penyusun Persamaan Reaksi Kimia")

if "selected_elements" not in st.session_state:
    st.session_state.selected_elements = []

# --- Tabel Periodik Interaktif ---
st.write("### Pilih 2 Unsur:")
for baris in elemen_periodik:
    cols = st.columns(len(baris))
    for i, elemen in enumerate(baris):
        simbol = elemen["simbol"]
        if simbol:
            if cols[i].button(simbol, key=simbol):
                if simbol not in st.session_state.selected_elements and len(st.session_state.selected_elements) < 2:
                    st.session_state.selected_elements.append(simbol)

# Tampilkan unsur terpilih
st.write(f"**Unsur Terpilih:** {', '.join(st.session_state.selected_elements)}")

if st.button("Reset Pilihan"):
    st.session_state.selected_elements = []
    st.rerun()

# --- Logika Penyusunan Reaksi ---
if len(st.session_state.selected_elements) == 2:
    kunci = frozenset(st.session_state.selected_elements)
    hasil = reaksi_database.get(kunci)

    if hasil:
        st.markdown("---")
        st.write("### Hasil Reaksi:")
        
        if "setara" in hasil:
            st.latex(hasil["setara"])
            mr = hitung_massa_molekul(hasil["produk"])
            st.info(f"Massa Molekul Relatif (Mr) {hasil['produk']}: {mr:.2f}")
        
        elif "setara_opsi" in hasil:
            st.write("Beberapa kemungkinan reaksi:")
            for i, opsi in enumerate(hasil["setara_opsi"]):
                st.latex(opsi)
                mr = hitung_massa_molekul(hasil["produk_opsi"][i])
                st.caption(f"Mr {hasil['produk_opsi'][i]}: {mr:.2f}")
    else:
        st.error("Reaksi untuk kombinasi unsur ini belum tersedia di database.")
