#Nama : Devin Nur Fauzan
#Absen : 08
#Kelas : XI TKJ 2
#Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
#Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def fibonacci(n):
    if n <= 0:
        return "Masukkan angka bulat positif"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
n = int(input("Masukkan nilai n untuk bilangan Fibonacci ke-n: "))
hasil_fibonacci = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil_fibonacci}.")