from prettytable import PrettyTable

# Membuat objek PrettyTable
menu_table = PrettyTable()
menu_table.field_names = ["Menu", "Harga (Rp)"]

# Menambahkan data menu dan harga ke dalam tabel
menu_harga = {
    'Nasi Goreng': 15000,
    'Mie Goreng': 12000,
    'Ayam Bakar': 25000,
    'Sate Ayam': 18000,
    'Bakso': 10000,
    'Soto Ayam': 12000,
    'Nasi Kuning': 14000,
    'Nasi Uduk': 16000
}

for menu, harga in menu_harga.items():
    menu_table.add_row([menu, harga])

# Menampilkan tabel
print("Daftar Menu dan Harga:")
print(menu_table)

# Contoh cara menghitung total harga pesanan
pesanan = ['Nasi Goreng', 'Ayam Bakar', 'Sate Ayam']
total_harga = sum(menu_harga[item] for item in pesanan)
print(f"Total Harga Pesanan: Rp {total_harga}")
