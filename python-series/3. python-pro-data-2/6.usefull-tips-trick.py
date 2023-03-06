# Tuple Length
print(">>> Tuple")
tuple_menu = ('Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak')
jumlah_menu = len(tuple_menu)
print(jumlah_menu)

# List Length
print(">>> List")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
jumlah_menu = len(list_menu)
print(jumlah_menu)

# Konversi tipe data
print(">>> Konversi tipe data")
list_buah = ['Apel', 'Apel', 'Jeruk', 'Markisa', 'Jeruk', 'Markisa', 'Apel']

# Melemparkan list ke dalam set() untuk mengkonversi sebuah list ke sebuah set
set_buah = set(list_buah)
print(set_buah)

# Melemparkan set ke dalam list() untuk mengkonversi sebuah set ke sebuah list
list_buah = list(set_buah)
list_buah.sort()
print(list_buah)

# trik ini akan sangat berguna ketika ingin mendapatkan seluruh list
# element unik pada bahasa pemrograman Python.
