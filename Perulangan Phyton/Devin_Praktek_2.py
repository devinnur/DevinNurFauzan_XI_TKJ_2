#Nama : Devin Nur Fauzan
#Kelas : XI TKJ 2
#Absen : 08
#Soal :Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai
#dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program
#yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10
#kilometer.
#Rumus: Jarak minggu ke-n = Jarak minggu ke-(n-1) + 10% dari Jarak minggu ke-(n-1)

jarak = 5  
target_jarak = 10  
minggu = 0 

while jarak <= target_jarak:
    minggu += 1
    pertambahan_jarak = jarak * 0.10 
    jarak += pertambahan_jarak

print(f"Pelari dapat berlari lebih dari {target_jarak} kilometer setelah {minggu} minggu.")