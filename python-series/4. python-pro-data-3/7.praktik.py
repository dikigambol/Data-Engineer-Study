# Aku tak pernah membayangkan diriku benar-benar mengerjakan program untuk kebutuhan perusahaan.
# Seperti sekarang, aku sedang mengerjakan rikues untuk memenuhi penghitungan pembayaran fee karyawan lepas.

# Tapi tak apa. Sejak program yang terakhir berhasil, aku sedikit lebih percaya diri untuk menjawab tantangan baru.

# Sembari menyeruput kopi hangat, aku mulai memasukkan informasi yang cukup

# untuk membuat class Tenaga Lepas berisi nama, usia, dan pendapatan selama bergabung di sebuah proyek.
# Lalu, apa lagi ya?

# “Nja, mau nanya. Kalau karyawan lepas, insentif tambahannya dari uang lembur juga?”

# “Engga, Aksara. Di kantor kita, karyawan lepas dapat insentif dari proyek yang dikerjakan.
# Kalau hasilnya sukses bisa dapat 1% dari nilai proyek.”

# “Oke,” aku mencatat itu sebagai penghitungan akhir dan mulai menulis kodenya.

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

# Definisikan class TenagaLepas sebagai child class dari
# class Karyawan
class TenagaLepas(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan, 0)

    def tambahan_proyek(self, nilai_proyek):
        self.pendapatan_tambahan += int(nilai_proyek * 0.01)

# Definisikan class AnalisData sebagai child class dari
# class Karyawan
class AnalisData(Karyawan): 
    pass

# Definisikan class IlmuwanData sebagai child class dari
# class Karyawan
class IlmuwanData(Karyawan):
    def tambahan_proyek(self, nilai_proyek): 
        self.pendapatan_tambahan += int(0.1 * nilai_proyek)

# Definisikan class PembersihData sebagai child class dari
# class TenagaLepas
class PembersihData(TenagaLepas): 
    pass

# Definisikan class DokumenterTeknis sebagai child class dari
# class TenagaLepas
class DokumenterTeknis(TenagaLepas):
    def tambahan_proyek(self, jumlah_tambahan): 
        return
