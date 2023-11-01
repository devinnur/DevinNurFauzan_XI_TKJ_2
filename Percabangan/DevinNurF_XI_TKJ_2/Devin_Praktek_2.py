# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# Soal: Buat program Python yang mengambil estimasi waktu selesai proyek dan tanggal target selesai. Jika estimasi waktu selesai lebih awal atau sama dengan tanggal target, program harus mencetak "Tepat waktu," jika tidak, program harus mencetak "Terlambat."
from datetime import datetime 
estimasi_selesai= datetime(2023, 10, 19)
tanggal_target= datetime(2023, 10, 25)
if estimasi_selesai <= tanggal_target:
    print("TEPAT WAKTU")
else:
    print("TELAT")