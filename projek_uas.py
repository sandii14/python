from prettytable import PrettyTable

class BaksoKumis:
    def __init__(self):
        self.menu = {
            'Bakso Rusuk': 35000,
            'Bakso Tetelan': 35000,
            'Bakso Tumpeng': 35000,
            'Bakso Spesial': 24000,
            'Bakso Urat': 15000,
            'Bakso Telur': 15000,
            'Bakso Kecil/Biasa': 15000,
            'Mie Ayam': 12000,
            'Mie Ayam Bakso Urat': 20000,
            'Mie Ayam Bakso Telur': 20000,
            'Mie Ayam Bakso Biasa': 20000,
            'Soto Ayam': 13000,
            'Kerupuk Bangka': 12000,
            'Jus Buah': 12000,
            'Es Campur': 12000,
            'Es Jeruk / Hangat': 7000,
            'Es Teh Tawar/Hangat': 2000,
            'Es Teh Manis/Hangat': 5000,
            'Teh Botol/S TEE': 6000,
            'Pop Ice': 6000,
            'Air Mineral': 4000,                                                                                                                                                                    
        }               
        self.pilihan = []

    def table_menu(self):
        print("\nMenu Bakso dan Minuman:")
        table = PrettyTable(["No", "Item", "Harga"])
        for i, (item, harga) in enumerate(self.menu.items(), start=1):
            table.add_row([i, item, f"Rp {harga}"])
        print(table)

    def proses_transaksi(self):
        print("\nProses Transaksi")
        total = 0
        while True:
            if not total:
                self.table_menu()
            print("\n---------------------------------------------------------------------")
            item_number = input("Pilih nomor menu (ketik 'N/n' untuk menyelesaikan transaksi): ")
            print("---------------------------------------------------------------------")
            if item_number == 'N' or item_number =="n":
                break
            
            try:
                item_number = int(item_number)
                if 1 <= item_number <= len(self.menu):
                    selected_item = list(self.menu.keys())[item_number - 1]
                    quantity = int(input(f"Jumlah {selected_item}: "))
                    total += self.menu[selected_item] * quantity
                    self.pilihan.append({"Item": selected_item,"Harga":self.menu[selected_item], "Quantity": quantity, "Subtotal": self.menu[selected_item] * quantity})
                else:
                    print("Nomor menu tidak tersedia. Silakan coba lagi.")
            except ValueError:
                print("Masukkan nomor menu yang tersedia.")

        return total

    def generate_receipt(self, total):
        print("\n\n             Bakso Kumis Permai  ")
        print("          Perum Babelan Mas Permai")
        print("\nDetail Pembelian")
        table = PrettyTable(["Item","Harga", "Quantity", "Subtotal"])
        for item in self.pilihan:
            table.add_row([item["Item"],item["Harga"], item["Quantity"], f"Rp {item['Subtotal']}"])
        print(table)


          
        print(f"\nJumlah Semua                 : Rp {total}")
        uang_diberikan = float(input("Cash                         : Rp "))
        kembalian = uang_diberikan - total
        print('------------------------------------------')
        print(f"Total Harga                  : Rp {total}")
        print(f"Uang Diberikan               : Rp {uang_diberikan}")
        print(f"Kembalian                    : Rp {kembalian if kembalian >= 0 else 'Uang tidak cukup'}")
        print('------------------------------------------')

        print("      Terima Kasih Atas Kunjungannya")
def main():
    bakso_kumis = BaksoKumis()

    while True:
        print("\n\n\n========================================")
        print("          Bakso Kumis Permai   ")
        print("        Perum Babelan Mas Permai ")
        print("========================================")
        print("        1. Proses Transaksi")
        print("        2. Keluar")
        print("----------------------------------------")

        choice = input("Pilih kategori: ")

        if choice == '1':
            total = bakso_kumis.proses_transaksi()
            bakso_kumis.generate_receipt(total)
            bakso_kumis.pilihan = []
        elif choice == '2':
            print("\nTerima kasih! Sampai jumpa.")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()

