# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# Soal: Buat program Python yang mengambil total belanjaan dan status anggota (biasa atau premium). Berikan diskon berdasarkan aturan berikut:
#Anggota premium: Jika total belanjaan lebih dari 500.000, berikan diskon 15%. Jika tidak, berikan diskon 10%.
#Anggota biasa: Jika total belanjaan lebih dari 300.000, berikan diskon 7%. Jika tidak, berikan diskon 0%.

total_Belanja= float(input("masukan total belanjaan anda: "))
status_anggota= input("masukan status anggota (oremium/tidak):").lower()
diskon = 0
if status_anggota == "premium":
    if total_Belanja > 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif status_anggota == "TIDAK":
    if total_Belanja > 300000:
        diskon = 0.07

jumlah_yang_harus_dibayar = total_Belanja - (total_Belanja*diskon)
print("jumlah yang harus dibayarkan: Rp", jumlah_yang_harus_dibayar)

