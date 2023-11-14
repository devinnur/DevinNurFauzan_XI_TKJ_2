#Nama : Devin Nur Fauzan
#Absen : 08
#Kelas : XI TKJ 2
#Soal : Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#batas tertentu yang ditentukan pengguna.
#Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)

def total_bilangan_ganjil(batas):
    total = sum(range(1, 2 * batas, 2))
    return total

batas = int(input("Masukkan batas deret bilangan ganjil: "))
total = total_bilangan_ganjil(batas)
print(f"Total deret bilangan ganjil sampai batas {batas} adalah {total}.")