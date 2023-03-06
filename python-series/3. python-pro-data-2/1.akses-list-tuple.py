bulan_pembelian = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
                   'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')

# Mengakses elemen pada suatu list ataupun tuple 
# dengan menggunakan indeks atau semacam nomor urut dari 
# list atau tuple tersebut. Indeks pada suatu tipe data list 
# atau tuple dimulai dari angka 0.
print(bulan_pembelian[0])
print(bulan_pembelian[5])
print(bulan_pembelian[-1])
print(bulan_pembelian[-2])

# Cara collections manipulation pertama yang akan aku pelajari adalah memotong 
# (slicing) list/tuple dengan menggunakan rentangan nilai indeks (range of index).
pertengahan_tahun = bulan_pembelian[4:8]
print(pertengahan_tahun)
awal_tahun = bulan_pembelian[:5]
print(awal_tahun)
akhir_tahun = bulan_pembelian[8:]
print(akhir_tahun)
print(bulan_pembelian[-4:-1])

# Penggabungan Dua atau Lebih List atau Tuple
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)
