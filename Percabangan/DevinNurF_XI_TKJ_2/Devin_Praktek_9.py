# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# SOAL: Buat program Python yang mengambil status persiapan proyek dan menentukan apakah proyek tersebut dapat diluncurkan. Jika status persiapan "Siap," program harus mencetak "Proyek diluncurkan." Jika status persiapan "Tunda," program harus mencetak "Proyek ditunda."
status_persiapan = input("Masukkan status persiapan proyek (Siap/Tunda): ").lower()

if status_persiapan == "siap":
    print("Proyek diluncurkan.")
elif status_persiapan == "tunda":
    print("Proyek ditunda.")
else:
    print("Status persiapan tidak valid. Harap masukkan 'Siap' atau 'Tunda'.")