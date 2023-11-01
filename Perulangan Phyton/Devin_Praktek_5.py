#Nama : Devin Nur Fauzan
#Kelas : XI TKJ 2
#Absen : 08
#Soal : Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan
#dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang
#menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.
#Rumus: Jumlah pembelahan setelah t menit = t / 20

waktu_total_menit = 120 
interval_pembelahan = 20  
jumlah_pembelahan = 0
waktu = 0
while waktu < waktu_total_menit:
    waktu += interval_pembelahan
    jumlah_pembelahan += 1
print(f"Jumlah pembelahan bakteri dalam jangka waktu 2 jam yaitu {jumlah_pembelahan} kali.")