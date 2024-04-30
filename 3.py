import pandas as pd
from prettytable import PrettyTable

# Membuat DataFrame dari daftar menu
data = {
    'Menu': ['Nasi Goreng', 'Mie Goreng', 'Ayam Bakar', 'Sate Ayam', 'Bakso'],
    'Harga (Rp)': [15000, 12000, 25000, 18000, 10000]
}
df_menu = pd.DataFrame(data)

# Membuat objek PrettyTable
menu_table = PrettyTable()
menu_table.field_names = ["Menu", "Harga (Rp)"]

# Menambahkan data dari DataFrame ke dalam tabel
for row in df_menu.itertuples(index=False):
    menu_table.add_row(row)

# Menampilkan tabel
print("Daftar Menu Makanan:")
print(menu_table)
