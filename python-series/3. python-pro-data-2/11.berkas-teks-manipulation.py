import requests
url = "https://storage.googleapis.com/dqlab-dataset/hello.txt"
response = requests.get(url)

# Cetak kode status dari response
print(response)

# Cetak isi file hello.txt menggunakan method response.iter_lines()
print("\n>> Cetak isi file hello.txt menggunakan method response.iter_lines():")
for baris in response.iter_lines():
    print(baris)

# Cetak isi file hello.txt menggunakan atribut response.text
print("\n>> Cetak isi file hello.txt menggunakan atribut response.text:")
print(response.text)

# Menulis ke file hello.txt
file = open('hello.txt', 'w')
file.write("Sekarang kita belajar menulis dengan menggunakan Python")
file.write("Menulis konten file dengan mode w (write).")
file.close()

# Menulis ke file dengan mode append
file = open('hello.txt', 'a')
file.writelines([
    "Sekarang kita belajar menulis dengan menggunakan Python",
    "Menulis konten file dengan mode a (append)"
])
file.close()
