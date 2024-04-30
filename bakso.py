from prettytable import PrettyTable

class BaksoKumis:
    def __init__(self):
        self.bakso_menu = {
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
        }
        self.minuman_menu = {
            'Jus Buah': 12000,
            'Es Campur': 12000,
            'Es Jeruk / Hangat': 7000,
            'Es Teh Tawar/Hangat': 2000,
            'Es Teh Manis/Hangat': 5000,
            'Teh Botol/S TEE': 6000,
            'Pop Ice': 6000,
            'Air Mineral': 4000,
        }
        self.mentah_menu = {
            'Bakso Urat': 8000,
            'Bakso Telur': 8000,
            'Bakso Biasa': 2000
        }
        self.cart = []

    def table_menu(self, menu, menu_name):
        table = PrettyTable(["No", "Item", "Harga"])
        for i, (item, price) in enumerate(menu.items(), start=1):
            table.add_row([i, item, f"Rp {price}"])
        print(f"\nMenu {menu_name}:\n{table}")

    def process_transaction(self):
        print("\nProses Transaksi:")
        total = 0
        while True:
            print("\nMenu Pilihan:")
            print("1. Bakso")
            print("2. Minuman")
            print("3. Bakso Kering/Mentah")
            print("4. Selesai")

            category_choice = input("Pilih kategori menu: ")

            if category_choice == '1':
                total += self.process_menu(self.bakso_menu, "Bakso")
            elif category_choice == '2':
                total += self.process_menu(self.minuman_menu, "Minuman")
            elif category_choice == '3':
                total += self.process_menu(self.mentah_menu, "Bakso Kering/Mentah")
            elif category_choice == '4':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")

        return total

    def process_menu(self, menu, menu_name):
        self.table_menu(menu, menu_name)
        total_category = 0
        while True:
            item_number = input("\nPilih nomor menu (ketik 'selesai' untuk kembali): ")
            
            if item_number.lower() == 'selesai':
                break
            
            try:
                item_number = int(item_number)
                if 1 <= item_number <= len(menu):
                    selected_item = list(menu.keys())[item_number - 1]
                    quantity = int(input(f"Jumlah {selected_item}: "))
                    total_category += menu[selected_item] * quantity
                    self.cart.append({"Item": selected_item, "Quantity": quantity, "Subtotal": menu[selected_item] * quantity})
                else:
                    print("Nomor menu tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Masukkan nomor menu yang valid.")

        return total_category

    def generate_receipt(self, total):
        print("\n             Bakso Kumis Permai  ")
        print("          Perum Babelan Mas Permai")
        print("Detail Pembelian :")
        table = PrettyTable(["Item", "Quantity", "Subtotal"])
        for item in self.cart:
            table.add_row([item["Item"], item["Quantity"], f"Rp {item['Subtotal']}"])
        print(table)

        # Proses pembayaran
        print(f"\nJumlah Semua: Rp {total}")
        uang_diberikan = float(input("Cash: "))
        kembalian = uang_diberikan - total

        print(f"\nTotal Harga: Rp {total}")
        print(f"Uang Diberikan: Rp {uang_diberikan}")
        print(f"Kembalian: Rp {kembalian if kembalian >= 0 else 'Uang tidak cukup'}")

        print("Terima Kasih Atas Kunjungannya")

def main():
    bakso_shop = BaksoKumis()

    while True:
        print("\n==========================")
        print("   Bakso Kumis Permai   ")
        print(" Perum Babelan Mas Permai ")
        print("==========================")
        print("1. Pilih Menu")
        print("2. Keluar")
        print("--------------------------")

        choice = input("Pilih kategori: ")

        if choice == '1':
            total = bakso_shop.process_transaction()
            bakso_shop.generate_receipt(total)
            bakso_shop.cart = []  # Reset keranjang setelah transaksi selesai
        elif choice == '2':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
