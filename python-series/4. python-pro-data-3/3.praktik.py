# Seperti biasa, aku selalu pusing setiap usai membaca teori data.
# “Gimana, Aksara?” tanya Senja tanpa memalingkan perhatian dari laptop.

# “Kayaknya butuh praktik deh,” sahutku.

# “Oke, ini coba kamu bikin sistem manajemen perusahaan sederhana pakai Object Oriented (OO) ya.
# Artinya dalam program ini kamu harus mampu memuat informasi nama, alamat, nomor telepon,
# dan daftar karyawan yang bekerja. Satu lagi, jangan lupa masukkan fungsi untuk mengaktifkan
# dan menonaktifkan karyawan.”

# “Siap. Ini aku masukkan informasi class karyawan juga kali yah?” tanyaku sembari bersiap-siap
# memasukkan kode dan mendaftar informasi karyawan secara lebih rapi, mulai dari nama,
# usia, pendapatan tetap, tambahan, dan insentif lembur.

# “Bagus juga itu. Bikin saja pendapatan mula-mula karyawannya bernilai 0, lalu bisa bertambah
# oleh fungsi lembur dan fungsi tambahan proyek sebagai parameter dan variabel pendapatan
# tambahan karyawan.”

# Aku mengangguk dan siap bertempur. Terakhir aku menyelipkan fungsi untuk menghitung total pendapatan.
# Ini paling penting, hehehe.

# Definisikan class Karyawan
class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = insentif_lembur

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan

# Definisikan class Perusahaan


class Perusahaan:
    def __init__(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = []

    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.append(karyawan)

    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.remove(karyawan_nonaktif)

# Definisikan perusahaan
perusahaan = Perusahaan('ABC', 'Jl.Jendral Sudirman, Blok 11', '(021) 95205XX')
# Definisikan nama-nama karyawan
karyawan_1 = Karyawan('Ani', 25, 8500000, 100000)
karyawan_2 = Karyawan('Budi', 28, 12000000, 150000)
karyawan_3 = Karyawan('Cici', 30, 15000000, 200000)
# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan_1)
perusahaan.aktifkan_karyawan(karyawan_2)
perusahaan.aktifkan_karyawan(karyawan_3)
