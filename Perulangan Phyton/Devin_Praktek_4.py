#Nama : Devin Nur Fauzan
#Kelas : XI TKJ 2
#Absen : 08
#Soal : Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
#jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
#apel kurang dari 20 buah.
#Rumus: Sisa apel hari ke-n = Sisa apel hari ke-(n-1) - 10% dari Sisa apel hari ke-(n-1)

jumlah_apel = 100  
target_sisa_apel = 8  
hari = 0  
while jumlah_apel > target_sisa_apel:
    hari += 1
    penjualan = jumlah_apel * 0.10  
    jumlah_apel -= penjualan

print(f"Sisa buah apel kurang dari {target_sisa_apel} buah setelah {hari} hari.")
