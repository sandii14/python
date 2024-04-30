from prettytable import PrettyTable

class BaksoShop:
    def __init__(self):
        self.menu = {
            'Bakso Biasa': 15000,
            'Bakso Spesial': 20000,
            'Bakso Super': 25000,
            'Es Teh Manis': 5000,
            'Air Mineral': 3000,
        }
        self.transactions = []
        self.current_transaction = None
        self.transaction_counter = 1

    def display_menu(self):
        table = PrettyTable(["No", "Item", "Harga"])
        for i, (item, price) in enumerate(self.menu.items(), start=1):
            table.add_row([i, item, f"Rp {price:,}"])
        print("\nMenu Bakso dan Minuman:")
        print(table)

    def start_transaction(self):
        self.current_transaction = {
            "Transaction Number": self.transaction_counter,
            "Items": [],
            "Total": 0,
        }
        self.transaction_counter += 1

    def process_transaction(self):
        print("\nProses Transaksi:")
        self.start_transaction()

        total = 0
        while True:
            if not total:
                self.display_menu()

            item_number = input("\nPilih nomor menu (ketik 'selesai' untuk menyelesaikan transaksi): ")
            
            if item_number.lower() == 'selesai':
                break
            
            try:
                item_number = int(item_number)
                if 1 <= item_number <= len(self.menu):
                    selected_item = list(self.menu.keys())[item_number - 1]
                    quantity = int(input(f"Jumlah {selected_item}: "))
                    subtotal = self.menu[selected_item] * quantity
                    total += subtotal
                    self.current_transaction["Items"].append({"Item": selected_item, "Quantity": quantity, "Subtotal": subtotal})
                else:
                    print("Nomor menu tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Masukkan nomor menu yang valid.")

        self.current_transaction["Total"] = total
        self.transactions.append(self.current_transaction)
        self.current_transaction = None

        return total

    def generate_receipt(self, total):
        current_transaction = self.transactions[-1]

        print(f"\nStruk Pembelian (Nomor Transaksi: {current_transaction['Transaction Number']}):")
        table = PrettyTable(["Item", "Quantity", "Subtotal"])
        for item in current_transaction["Items"]:
            table.add_row([item["Item"], item["Quantity"], f"Rp {item['Subtotal']:,}"])
        print(table)

        

        # Proses pembayaran

        print(f"\nTotal Harga: Rp {total:,}")

        uang_diberikan = float(input("Jumlah uang yang diberikan: "))
        kembalian = uang_diberikan - total

        print(f"Uang Diberikan: Rp {uang_diberikan:,}")
        print(f"Kembalian: Rp {kembalian if kembalian >= 0 else 'Uang tidak cukup'}")

        print("Terima kasih telah berbelanja di Bakso Shop!")

    def show_transaction_history(self):
        print("\nRiwayat Transaksi:")
        total_semua_transaksi = 0
        for transaction in self.transactions:
            total_semua_transaksi += transaction['Total']
            print(f"\nNomor Transaksi: {transaction['Transaction Number']}")
            table = PrettyTable(["Item", "Quantity", "Subtotal"])
            for item in transaction["Items"]:
                table.add_row([item["Item"], item["Quantity"], f"Rp {item['Subtotal']:,}"])
            print(table)
            print(f"Total Harga: Rp {transaction['Total']:,}")
            print("=" * 40)

        print("\nTotal Semua Transaksi: Rp {total_semua_transaksi:,}")

def main():
    bakso_shop = BaksoShop()

    while True:
        print("\n=== Bakso Shop ===")
        print("1. Proses Transaksi")
        print("2. Lihat Riwayat Transaksi")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == '1':
            total = bakso_shop.process_transaction()
            bakso_shop.generate_receipt(total)
        elif choice == '2':
            bakso_shop.show_transaction_history()
        elif choice == '3':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
