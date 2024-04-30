class Converter:
    @staticmethod
    def decimal_to_binary(decimal):
        return bin(decimal)[2:]

    @staticmethod
    def decimal_to_octal(decimal):
        return oct(decimal)[2:]

    @staticmethod
    def decimal_to_hexadecimal(decimal):
        return hex(decimal)[2:]

def main():
    print("Konverter Sistem Bilangan")
    decimal = int(input("Masukkan bilangan desimal: "))

    binary = Converter.decimal_to_binary(decimal)
    octal = Converter.decimal_to_octal(decimal)
    hexadecimal = Converter.decimal_to_hexadecimal(decimal)

    print(f"Bilangan biner: {binary}")
    print(f"Bilangan oktal: {octal}")
    print(f"Bilangan heksadesimal: {hexadecimal}")

if __name__ == "__main__":
    main()