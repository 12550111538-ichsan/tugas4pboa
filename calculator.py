class Calculator:
    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    def bagi(self, a, b):
        if b == 0:
            raise ValueError("Tidak bisa membagi dengan nol")
        return a / b


# Program utama (opsional untuk interaksi user)
if __name__ == "__main__":
    calc = Calculator()
    
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        operasi = input("Pilih operasi (+, -, *, /): ")

        if operasi == "+":
            print("Hasil:", calc.tambah(a, b))
        elif operasi == "-":
            print("Hasil:", calc.kurang(a, b))
        elif operasi == "*":
            print("Hasil:", calc.kali(a, b))
        elif operasi == "/":
            print("Hasil:", calc.bagi(a, b))
        else:
            print("Operasi tidak valid")

    except ValueError:
        print("Input harus berupa angka!")