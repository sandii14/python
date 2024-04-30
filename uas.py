from prettytable import PrettyTable

class Converter:
    #converter desimal
    @staticmethod
    def decimal_to_binary(decimal):
        return f"{bin(decimal)[2:]} (biner)"

    @staticmethod
    def decimal_to_octal(decimal):
        return f"{oct(decimal)[2:]} (oktal)"

    @staticmethod
    def decimal_to_hexadecimal(decimal):
        return f"{hex(decimal)[2:]} (heksadesimal)"
    
    #converter biner
    @staticmethod
    def binary_to_decimal(binary):
         return f"{int(str(binary),2)} (decimal)"

    @staticmethod
    def binary_to_octal(binary):
        octal = int(str(binary), 2)
        return f"{oct(octal)[2:]} (oktal)"

    @staticmethod
    def binary_to_hexadecimal(binary):
        hexa = int(str(binary), 2)
        return f"{hex(hexa)[2:]} (oktal)"
    
    #converter octal
    @staticmethod
    def octal_to_decimal(octal):
         return f"{int(str(octal),8)} (decimal)"

    @staticmethod
    def octal_to_binary(octal):
        binary = int(str(octal), 8)
        return f"{bin(binary)[2:]} (biner)"

    @staticmethod
    def octal_to_hexadecimal(octal):
        hexa = int(str(octal), 8)
        return f"{hex(hexa)[2:]} (oktal)"

    
    #converter hexa
    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
         return f"{(int(str(hexadecimal),16))} (decimal)"

    @staticmethod
    def hexadecimal_to_binary(hexadecimal):
        binary = int(str(hexadecimal), 16)
        return f"{bin(binary)[2:]} (biner)"

    @staticmethod
    def hexadecimal_to_octal(hexadecimal):
        octal = int(str(hexadecimal), 16)
        return f"{oct(octal)[2:]} (oktal)"

class SistemBilangan:
    def __init__(self):
        self.desimal = [
            {'No': 1, 'Pilihan': 'desimal to biner'},
            {'No': 2, 'Pilihan': 'desimal to oktal'},
            {'No': 3, 'Pilihan': 'desimal to hexa'}
        ]
        self.pilihan = []
        self.biner = [
            {'No': 1, 'Pilihan': 'biner to desimal'},
            {'No': 2, 'Pilihan': 'biner to oktal'},
            {'No': 3, 'Pilihan': 'biner to hexa'}
        ]
        self.pilihan = []
        self.oktal = [
            {'No': 1, 'Pilihan': 'oktal to desimal'},
            {'No': 2, 'Pilihan': 'oktal to biner'},
            {'No': 3, 'Pilihan': 'oktal to hexa'}
        ]
        self.pilihan = []
        self.hexadecimal = [
            {'No': 1, 'Pilihan': 'hexadecimal to desimal'},
            {'No': 2, 'Pilihan': 'hexadecimal to biner'},
            {'No': 3, 'Pilihan': 'hexadecimal to octal'}
        ]
        self.pilihan = []

    def display_menu(self):
        print("\n\n\n========================================")
        print("          SISTEM BILANGAN   ")
        print("         KALKULATOR SISTEM BILANGAN ")
        print("========================================")
        print("        1. Desimal")
        print("        2. Biner")
        print("        3. Oktal")
        print("        4. Hexadesimal")
        print("        5. Keluar")
        print("----------------------------------------")

    #konversi desimal
    def options_decimal(self):
        print("\nKonversi Bilangan:")
        table = PrettyTable(["No", "Pilihan"])
        for item in self.desimal:
            table.add_row([item['No'], item['Pilihan']])
        print(table)

    def convert_decimal(self, number, base):
        if base == 1:
            return Converter.decimal_to_binary(number)
        elif base == 2:
            return Converter.decimal_to_octal(number)
        elif base == 3:
            return Converter.decimal_to_hexadecimal(number)
        else:
            return "Basis bilangan tidak valid"
        
        #konversi biner
    def options_binary(self):
        print("\nKonversi Bilangan:")
        table = PrettyTable(["No", "Pilihan"])
        for item in self.biner:
            table.add_row([item['No'], item['Pilihan']])
        print(table)

    def convert_binary(self, number, base):
        if base == 1:
            return Converter.binary_to_decimal(number)
        elif base == 2:
            return Converter.binary_to_octal(number)
        elif base == 3:
            return Converter.binary_to_hexadecimal(number)
        else:
            return "Basis bilangan tidak valid"
        
         #konversi oktal
    def options_octal(self):
        print("\nKonversi Bilangan:")
        table = PrettyTable(["No", "Pilihan"])
        for item in self.oktal:
            table.add_row([item['No'], item['Pilihan']])
        print(table)

    def convert_octal(self, number, base):
        if base == 1:
            return Converter.octal_to_decimal(number)
        elif base == 2:
            return Converter.octal_to_binary(number)
        elif base == 3:
            return Converter.octal_to_hexadecimal(number)
        else:
            return "Basis bilangan tidak valid"
        
        #konversi hexa
    def options_hexadecimal(self):
        print("\nKonversi Bilangan:")
        table = PrettyTable(["No", "Pilihan"])
        for item in self.hexadecimal:
            table.add_row([item['No'], item['Pilihan']])
        print(table)

    def convert_hexadecimal(self, number, base):
        if base == 1:
            return Converter.hexadecimal_to_decimal(number)
        elif base == 2:
            return Converter.hexadecimal_to_binary(number)
        elif base == 3:
            return Converter.hexadecimal_to_octal(number)
        else:
            return "Basis bilangan tidak valid"

    
    def process_choice(self, choice):
        if choice == 1:
            self.options_decimal()
            convert_choice = input("Pilih konversi: ")
            if convert_choice in ['1', '2', '3']:
                number = int(input("Masukkan bilangan desimal: "))
                print(f"Hasil konversi: {self.convert_decimal(number, int(convert_choice))}")
            else:
                print("bilangan tidak valid.")

        elif choice == 2:
            self.options_binary()
            convert_choice = input("Pilih konversi: ")
            if convert_choice in ['1', '2', '3']:
                number = int(input("Masukkan bilangan biner: "))
                print(f"Hasil konversi: {self.convert_binary(number, int(convert_choice))}")
            else:
                print("bilangan tidak valid.")

        elif choice == 3:
            self.options_octal()
            convert_choice = input("Pilih konversi: ")
            if convert_choice in ['1', '2', '3']:
                number = int(input("Masukkan bilangan octal: "))
                print(f"Hasil konversi: {self.convert_octal(number, int(convert_choice))}")
            else:
                print("bilangan tidak valid.")

        elif choice == 4:
            self.options_hexadecimal()
            convert_choice = input("Pilih konversi: ")
            if convert_choice in ['1', '2', '3']:
                number = input("Masukkan bilangan hexadesimal: ")
                print(f"Hasil konversi: {self.convert_hexadecimal(number, int(convert_choice))}")
            else:
                print("bilangan tidak valid.")

        elif choice == 5:
                print("\nConverter")
                print("Terima Kasih")

        else:
            print("\nPilihan tidak valid. Silakan pilih lagi.")
            
def main():
    menu = SistemBilangan()

    while True:
        menu.display_menu()
        choice = input("Pilih kategori: ")

        try:
            choice = int(choice)
            if choice in [1, 2, 3, 4, 5]:
                menu.process_choice(choice)
            else:
                print("Pilihan tidak valid. Silakan pilih lagi.")
        except ValueError:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
