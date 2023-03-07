-- Mengambil Seluruh Kolom dalam suatu Tabel
SELECT * FROM tabel

-- Mengambil Satu Kolom dari Tabel
SELECT kolom FROM tabel

-- Mengambil Lebih dari Satu Kolom dari Tabel
SELECT kolom1, kolom2 FROM tabel

-- Membatasi Pengambilan Jumlah Row Data
SELECT kolom1, kolom2 FROM tabel LIMIT 5

-- Penggunaan SELECT DISTINCT statement
-- Untuk menghilangkan data duplikasi, aku bisa menggunakan SELECT DISTINCT statement. Dengan SELECT DISTINCT, 
-- data yang sama atau duplikat akan dieliminasi dan akan ditampilkan data yang unik saja.
SELECT DISTINCT kolom1, kolom2 FROM tabel

-- Menggunakan Prefix pada Nama Kolom
SELECT tabel.kolom FROM tabel

-- Menggunakan Alias pada Kolom
SELECT kolom1 AS alias, kolom2 AS alias2 FROM tabel

SELECT kolom1 alias, kolom2 alias2 FROM tabel

-- Menggabungkan Prefix dan Alias
SELECT tabel.kolom AS alias FROM tabel

-- Menggunakan Alias pada Tabel
SELECT * FROM tabel alias

-- Prefix dengan Alias Tabel
SELECT alias.kolom1, alias.kolom2 FROM tabel alias

-- Menggunakan WHERE
SELECT * FROM tabel WHERE kolom = 'condition'

-- Menggunakan Operand OR
SELECT * FROM tabel WHERE kolom = 'kondisi1' 
OR kolom2 = 'kondisi2' OR kolom3 = 'kondisi3'

-- Filter untuk Angka
SELECT * FROM tabel WHERE kolom > 50000

-- Menggunakan Operand AND
SELECT * FROM tabel WHERE kolom = 'kondisi' AND kolom2 < 50000
