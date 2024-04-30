import pandas as pd

# Fungsi untuk menampilkan DataFrame
def tampilkan_data(dataframe):
    print(dataframe)

# Membaca data dari file Excel saat program dimulai
def baca_data():
    try:
        df = pd.read_excel('data.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Nama', 'Usia'])
    return df

# Fungsi untuk menambahkan data baru
def tambah_data(dataframe, nama, usia):
    new_data = pd.DataFrame({'Nama': [nama], 'Usia': [usia]})
    dataframe = pd.concat([dataframe, new_data], ignore_index=True)
    dataframe.to_excel('data.xlsx', index=False)
    return dataframe

# Fungsi untuk memperbarui data
def perbarui_data(dataframe, index, kolom, nilai):
    dataframe.at[index, kolom] = nilai
    dataframe.to_excel('data.xlsx', index=False)
    return dataframe

# Fungsi untuk menghapus data
def hapus_data(dataframe, index):
    dataframe = dataframe.drop(index)
    dataframe.to_excel('data.xlsx', index=False)
    return dataframe

# Contoh penggunaan
df = baca_data()

while True:
    print("\nMenu:")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Perbarui Data")
    print("4. Hapus Data")
    print("5. Keluar")
    pilihan = input("Pilih opsi (1/2/3/4/5): ")

    if pilihan == '1':
        tampilkan_data(df)
    elif pilihan == '2':
        nama = input("Masukkan nama: ")
        usia = int(input("Masukkan usia: "))
        df = tambah_data(df, nama, usia)
    elif pilihan == '3':
        index = int(input("Masukkan indeks baris yang akan diperbarui: "))
        kolom = input("Masukkan nama kolom yang akan diperbarui: ")
        nilai = input("Masukkan nilai baru: ")
        df = perbarui_data(df, index, kolom, nilai)
    elif pilihan == '4':
        index = int(input("Masukkan indeks baris yang akan dihapus: "))
        df = hapus_data(df, index)
    elif pilihan == '5':
        break
