# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# Soal: Buat program Python yang mengambil total belanjaan pelanggan dan memberikan diskon  berdasarkan aturan berikut
total_belanjaan = float(input("Total_belanjaan Anda: "))
if total_belanjaan > 500000:
    diskon = total_belanjaan*0.10
elif total_belanjaan >= 300000:
    diskon = total_belanjaan *0.05
else:
    diskon = 0
total_pembayaran = total_belanjaan - diskon
print("Total pembayaran setelah diskon: (total pembayaran)")