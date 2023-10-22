# Nama: Devin Nur Fauzan
# Kelas: XI TKJ 2
# Absen: 08
# Soal:Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan:
#• Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris."
#• Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer."
#• Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."

penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))
if penjualan > 1000:
    kategori = "Produk Terlaris"
elif 500 <= penjualan <= 1000:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"
print(f"Kategori produk: {kategori}")