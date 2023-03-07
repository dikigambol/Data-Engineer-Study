#Buatlah factor dengan isi nilai teks "Jan", "Feb", dan "Mar"
factor(c("Jan","Feb","Mar"))

#Variable factor bernama faktor.bulan dengan nilai teks "Jan", "Feb", dan "Mar"
faktor.bulan <-factor(c("Jan","Feb","Mar"))
attributes(faktor.bulan)
levels(faktor.bulan)
class(faktor.bulan)

#Buatlah factor dengan teks "Jan", "Feb", "Mar","Jan","Mar", dan "Jan"
factor(c("Jan","Feb","Mar","Jan","Mar","Jan"))

# Penjelasan dari proses di atas :
# 1. R menerima perintah dengan function factor(c("Jan","Feb","Mar","Jan","Mar"))
# 2. R akan mencari variasi nilai (levels) dan diurutkan – dalam hal ini pengurutan 
# alfabet – dan dipetakan berdasarkan index yang bernilai integer.Disini nilai index 1 
# mewakili "Feb", 2 mewakili "Jan", dan 3 mewakili "Mar"
# 3. Dari levels, nilai-nilai "Jan", "Feb", "Mar","Jan","Mar" dicari nilai index-nya dan 
# dimasukkan sebagai nilai-nilai pada factor ( 2, 1, 3, 2, 3).

# Dengan demikian, kita simpulkan kembali dari ilustrasi di atas bahwa nilai dari 
# factor sebenarnya adalah nilai bilangan bulat (integer) dengan nilai-nilai kategoris 
# disimpan pada atribut levels.

#Buatlah factor dengan teks "Jan", "Feb", "Mar","Jan","Mar", dan "Jan"
factor.bulan <- factor(c("Jan","Feb","Mar","Jan","Mar","Jan"))
as.integer(factor.bulan)

#Mengganti levels 
levels(factor.bulan)[2] <- "Januari"
levels(factor.bulan)[3] <- "Maret"
factor.bulan

#Buatlah factor bernama factor.umur dengan isi c(12, 35, 24, 12, 35, 37)
factor.umur <- factor(c(12, 35, 24, 12, 35, 37))
#Tampilkan variable factor.umur 
factor.umur

#Buatlah variable factor.lokasi dengan isi berupa vector c("Bandung", "Jakarta", NA, "Jakarta", NaN, "Medan", NULL, NULL, "Bandung") 
factor.lokasi <- factor(c("Bandung", "Jakarta", NA, "Jakarta", NaN, "Medan", NULL, NULL, "Bandung"))

#Tampilkan factor.lokasi
factor.lokasi

#Tampilkan panjang dari variable factor.lokasi
length(factor.lokasi)

#Variable factor dengan isi vector c("Jan","Feb","Mar","Jan","Mar") 
factor(c("Jan","Feb","Mar","Jan","Mar"), levels = c("Jan", "Feb", "Mar"))

