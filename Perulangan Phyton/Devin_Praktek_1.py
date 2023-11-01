#Nama : Devin Nur Fauzan
#Kelas : XI TKJ 2
#Absen : 08
#Soal : Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah
#ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung
#berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.
#Rumus: Jumlah ayam bulan ke-n = Jumlah ayam bulan ke-(n-1) + 5% dari Jumlah ayam bulan ke-(n-1)

jumlah_ayam = 100  
target_ayam = 200 
bulan = 0  

while jumlah_ayam <= target_ayam:
    bulan += 1
    pertambahan_ayam = jumlah_ayam * 0.05 
    jumlah_ayam += pertambahan_ayam

print(f"Jumlah ayam melebihi {target_ayam} ekor setelah {bulan} bulan.")
