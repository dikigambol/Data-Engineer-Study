nama_depan = 'John'
nama_belakang = 'Doee'
# Operator “+” untuk Tipe Data String
nama_lengkap = nama_depan + ' ' + nama_belakang
print(nama_lengkap)
umur = '27 tahun'
alamat = 'Jl. Anggrek No. 100'
nama_umur_alamat = 'Hi, saya ' + nama_lengkap + \
    ' umur ' + umur + ' , tinggal di ' + alamat + '.'
print(nama_umur_alamat)

# Menghilangkan Spasi
# Fitur .strip()
print(">>> Fitur .strip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.strip()
print(kata_sambutan)
# Fitur .lstrip()
print(">>> Fitur .lstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.lstrip()
print(kata_sambutan)
# Fitur .rstrip()
print(">>> Fitur .rstrip()")
kata_sambutan = ' halo, selamat siang! '
kata_sambutan = kata_sambutan.rstrip()
print(kata_sambutan)

# Merubah Caps pada String
# Fitur .capitalize()
print(">>> Fitur .capitalize()")
judul_buku = 'belajar bahasa Python'
print(judul_buku.capitalize())
# Fitur .lower()
print(">>> Fitur .lower()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.lower())
# Fitur .upper()
print(">>> Fitur .upper()")
judul_buku = 'Belajar Bahasa PYTHON.'
print(judul_buku.upper())

# Pemecahan, Penggabungan, dan Penggantian String
# Fitur .split()
print(">>> Fitur .split()")
frasa = "ani dan budi dan wati dan johan"
karakter = frasa.split('dan')
print(karakter)
kata = frasa.split(' ')
print(kata)
# Fitur .join()
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
frasa = pemisah.join(karakter)
print(frasa)
frasa = " ".join(karakter)
print(frasa)
# Fitur .replace()
print(">>> Fitur .replace()")
frasa = "apel malang apel yang paling segar, apel sehat, apel nikmat"
frasa = frasa.replace('apel', 'jeruk')
print(frasa)

# Menentukan Posisi dan Jumlah Sub-string pada String
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
# Fitur .find()
print(">>> Fitur .find()")
print(teks.find('Apel'))
print(teks.find('malang'))
# Fitur .count()
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count('Apel')
print(kemunculan_kata_apel)

# Menentukan String Apakah Diawali/Diakhiri oleh Sub-string
# Fitur .startswith()
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel-apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))
# Fitur .endswith()
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))