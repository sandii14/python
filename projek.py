# Program penjualan bakso
# Membuat daftar menu dan harga
menu = ["Bakso biasa", "Bakso urat", "Bakso telur", "Bakso keju"]
harga = [10000, 12000, 15000, 18000]

# Membuat fungsi untuk menampilkan menu dan harga
def tampil_menu():
    print("Menu Bakso:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]} - Rp {harga[i]}")

# Membuat fungsi untuk menghitung total harga
def hitung_total(pesanan):
    total = 0
    for p in pesanan:
        total += harga[p-1]
    return total

# Membuat fungsi untuk menghitung kembalian
def hitung_kembalian(total, bayar):
    kembalian = bayar - total
    return kembalian

# Membuat fungsi untuk menampilkan struk
def tampil_struk(pesanan, total, bayar, kembalian):
    print("Struk Pembayaran:")
    print("Pesanan:")
    for p in pesanan:
        print(f"- {menu[p-1]} - Rp {harga[p-1]}")
    print(f"Total: Rp {total}")
    print(f"Bayar: Rp {bayar}")
    print(f"Kembalian: Rp {kembalian}")

# Membuat program utama
print("Selamat datang di Bakso Enak")
tampil_menu()
pesanan = []
lanjut = True
while lanjut:
    pilih = int(input("Masukkan nomor menu yang ingin dipesan: "))
    if pilih >= 1 and pilih <= len(menu):
        pesanan.append(pilih)
        print(f"Anda memesan {menu[pilih-1]}")
    else:
        print("Nomor menu tidak valid")
    jawab = input("Apakah Anda ingin memesan lagi? (y/n) ")
    if jawab.lower() == "n":
        lanjut = False
total = hitung_total(pesanan)
print(f"Total harga pesanan Anda adalah Rp {total}")
bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))
kembalian = hitung_kembalian(total, bayar)
tampil_struk(pesanan, total, bayar, kembalian)
print("Terima kasih telah berbelanja di Bakso Enak")
