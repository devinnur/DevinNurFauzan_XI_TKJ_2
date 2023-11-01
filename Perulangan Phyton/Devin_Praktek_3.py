#Nama : Devin Nur Fauzan
#Kelas : XI TKJ 2
#Absen : 08
#Soal : Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
#tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
#melebihi 20.000 dollar.
#Rumus: Nilai investasi tahun ke-n = Nilai investasi tahun ke-(n-1) + 6% dari Nilai investasi tahun ke-(n-1)

nilai_investasi = 10000  
target_nilai = 20000  
tahun = 0 
while nilai_investasi <= target_nilai:
    tahun += 1
    pertumbuhan_investasi = nilai_investasi * 0.06  
    nilai_investasi += pertumbuhan_investasi

print(f"Nilai investasi melebihi {target_nilai} dollar setelah {tahun} tahun.")
