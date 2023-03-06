# Statement if ==============================================================================>
x = 4
if x % 2 == 0:  # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")  # statemen aksi lebih menjorok ke dalam
# Statement if ... elif ... else
x = 7
if x % 2 == 0:  # jika sisa bagi x dengan 2 sama dengan 0
    print("x habis dibagi dua")
elif x % 3 == 0:  # jika sisa bagi x dengan 3 sama dengan 0
    print("x habis dibagi tiga")
elif x % 5 == 0:  # jika sisa bagi x dengan 5 sama dengan 0
    print("x habis dibagi lima")
else:
    print("x tidak habis dibagi dua, tiga, ataupun lima")

jam = 13
if jam >= 5 and jam <= 12:  # selama jam di antara 5 s.d. 12
    print("Selamat pagi!")
elif jam >= 12 and jam <= 17:  # selama jam di antara 12 s.d. 17
    print("Selamat siang!")
elif jam >= 17 and jam <= 19:  # selama jam di antara 17 s.d. 19
    print("Selamat sore!")
else:  # selain kondisi di atas
    print("Selamat malam!")


tagihan_ke = 'Mr. Yoyo'
warehousing = {'harga_harian': 1000000, 'total_hari': 15}
cleansing = {'harga_harian': 1500000, 'total_hari': 10}
integration = {'harga_harian': 2000000, 'total_hari': 15}
transform = {'harga_harian': 2500000, 'total_hari': 10}
sub_warehousing = warehousing['harga_harian'] * warehousing['total_hari']
sub_cleansing = cleansing['harga_harian'] * cleansing['total_hari']
sub_integration = integration['harga_harian'] * integration['total_hari']
sub_transform = transform['harga_harian'] * transform['total_hari']
total_harga = sub_warehousing + sub_cleansing + sub_integration + sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
print("Selamat pagi, anda harus membayar tagihan sebesar:")
print(total_harga)

jam = 17
tagihan_ke = 'Mr. Yoyo'
warehousing = {'harga_harian': 1000000, 'total_hari': 15}
cleansing = {'harga_harian': 1500000, 'total_hari': 10}
integration = {'harga_harian': 2000000, 'total_hari': 15}
transform = {'harga_harian': 2500000, 'total_hari': 10}
sub_warehousing = warehousing['harga_harian']*warehousing['total_hari']
sub_cleansing = cleansing['harga_harian']*cleansing['total_hari']
sub_integration = integration['harga_harian']*integration['total_hari']
sub_transform = transform['harga_harian']*transform['total_hari']
total_harga = sub_warehousing+sub_cleansing+sub_integration+sub_transform
print("Tagihan kepada:")
print(tagihan_ke)
if jam > 19:
    print("Selamat malam, anda harus membayar tagihan sebesar:")
elif jam > 17:
    print("Selamat sore, anda harus membayar tagihan sebesar:")
elif jam > 12:
    print("Selamat siang, anda harus membayar tagihan sebesar:")
else:
    print("Selamat pagi, anda harus membayar tagihan sebesar:")
print(total_harga)
# statement else if ===========================================================================>