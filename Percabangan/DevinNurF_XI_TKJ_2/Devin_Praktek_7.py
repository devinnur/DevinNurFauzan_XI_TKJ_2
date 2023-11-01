# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# Soal: Buat program Python yang mengambil informasi pembaruan perangkat lunak dan menentukan apakah sistem perlu di-restart. Jika pembaruan mengharuskan restart, program harus mencetak "Sistem perlu di-restart." Jika tidak, program harus mencetak "Sistem tidak perlu di-restart."

perlu_direstart = input("apakah KOMPUTER anda perlu direstart? (Iya/Tidak)")
if perlu_direstart.lower()=="iya":
    print("KOMPUTER di-Restart")
else:
    print("KOMPUTER tidak perlu direstart")
    