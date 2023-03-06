# Kode awal
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = 1 - potongan_harga
harga_bayar *= total_harga
pajak_bayar = pajak * harga_bayar
harga_bayar += pajak_bayar
print("Kode awal - harga_bayar=", harga_bayar)

# Penyederhanaan baris kode dengan menerapkan prioritas operator
total_harga = 150000
potongan_harga = 0.3
pajak = 0.1 # pajak dalam persen ~ 10%
harga_bayar = (1 - potongan_harga) * total_harga
harga_bayar += harga_bayar * pajak
print("Penyederhanaan kode - harga_bayar=", harga_bayar)