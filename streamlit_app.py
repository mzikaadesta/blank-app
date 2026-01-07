# --- DATABASE AR UNSUR ---
massa_atom = {
    "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, 
    "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "Ne": 20.18,
    "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97,
    "S": 32.07, "Cl": 35.45, "Ar": 39.95, "K": 39.10, "Ca": 40.08,
    "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00, "Mn": 54.94,
    "Fe": 55.85, "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38,
    "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.96, "Br": 79.90,
    "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22,
    "Nb": 92.91, "Mo": 95.95, "Tc": 98.00, "Ru": 101.07, "Rh": 102.91,
    "Pd": 106.42, "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71,
    "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91,
    "Ba": 137.33, "Pb": 207.2, "Bi": 208.98, "Po": 209.00, "At": 210.00,
    "Rn": 222.00
}# --- DATABASE LAYOUT TABEL PERIODIK ---
elemen_periodik = [
    # Baris 1
    [{"simbol": "H", "golongan": "IA"}, {"simbol": "", "golongan": ""}, {"simbol": "", "golongan": ""}, {"simbol": "", "golongan": ""}, {"simbol": "", "golongan": ""}, {"simbol": "", "golongan": ""}, {"simbol": "", "golongan": ""}, {"simbol": "He", "golongan": "VIIIA"}],
    # Baris 2
    [{"simbol": "Li", "golongan": "IA"}, {"simbol": "Be", "golongan": "IIA"}, {"simbol": "B", "golongan": "IIIA"}, {"simbol": "C", "golongan": "IVA"}, {"simbol": "N", "golongan": "VA"}, {"simbol": "O", "golongan": "VIA"}, {"simbol": "F", "golongan": "VIIA"}, {"simbol": "Ne", "golongan": "VIIIA"}],
    # Baris 3
    [{"simbol": "Na", "golongan": "IA"}, {"simbol": "Mg", "golongan": "IIA"}, {"simbol": "Al", "golongan": "IIIA"}, {"simbol": "Si", "golongan": "IVA"}, {"simbol": "P", "golongan": "VA"}, {"simbol": "S", "golongan": "VIA"}, {"simbol": "Cl", "golongan": "VIIA"}, {"simbol": "Ar", "golongan": "VIIIA"}],
    # Baris 4 (Contoh Logam Transisi)
    [{"simbol": "K", "golongan": "IA"}, {"simbol": "Ca", "golongan": "IIA"}, {"simbol": "Fe", "golongan": "Logam Transisi"}, {"simbol": "Cu", "golongan": "Logam Transisi"}, {"simbol": "Zn", "golongan": "Logam Transisi"}, {"simbol": "Ag", "golongan": "Logam Transisi"}, {"simbol": "Pb", "golongan": "IVA"}, {"simbol": "Kr", "golongan": "VIIIA"}]
]# --- DATABASE REAKSI KIMIA ---
# Menggunakan frozenset agar urutan klik unsur tidak berpengaruh (H+O sama dengan O+H)
reaction_rules = {
    frozenset(["H", "O"]): {
        "produk": "H2O", 
        "produk_latex": "H_2O", 
        "setara": "2H_2 + O_2 \\rightarrow 2H_2O", 
        "jenis": "Reaksi Sintesis (Pembentukan Air)"
    },
    frozenset(["Na", "Cl"]): {
        "produk": "NaCl", 
        "produk_latex": "NaCl", 
        "setara": "2Na + Cl_2 \\rightarrow 2NaCl", 
        "jenis": "Reaksi Sintesis (Garam Dapur)"
    },
    frozenset(["Fe", "Cl"]): {
        "produk_opsional": ["FeCl2", "FeCl3"],
        "produk_latex_opsi": ["FeCl_2", "FeCl_3"],
        "setara_opsi": ["Fe + Cl_2 \\rightarrow FeCl_2", "2Fe + 3Cl_2 \\rightarrow 2FeCl_3"],
        "jenis": "Reaksi Sintesis (Besi Klorida)"
    },
    frozenset(["C", "O"]): {
        "produk_opsional": ["CO", "CO2"],
        "produk_latex_opsi": ["CO", "CO_2"],
        "setara_opsi": ["2C + O_2 \\rightarrow 2CO", "C + O_2 \\rightarrow CO_2"],
        "jenis": "Reaksi Pembakaran Karbon"
    },
    frozenset(["Mg", "O"]): {
        "produk": "MgO", 
        "produk_latex": "MgO", 
        "setara": "2Mg + O_2 \\rightarrow 2MgO", 
        "jenis": "Reaksi Oksidasi Logam"
    },
    frozenset(["Cu", "S"]): {
        "produk": "CuS", 
        "produk_latex": "CuS", 
        "setara": "Cu + S \\rightarrow CuS", 
        "jenis": "Reaksi Pembentukan Tembaga Sulfida"
    }
}
