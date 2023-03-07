library(openxlsx)
library(reshape2)
penduduk.dki.xlsx <- read.xlsx(xlsxFile="https://storage.googleapis.com/dqlab-dataset/dkikepadatankelurahan2013.xlsx")

penduduk.dki.transform <- melt(data=penduduk.dki.xlsx, id.vars=c( "NAMA.KECAMATAN", "NAMA.KELURAHAN"), measure.vars = c("35-39.Laki-Laki", "35-39.Perempuan"), variable.name = "DEMOGRAFIK", value.name="JUMLAH")

#Memecah isi kolom DEMOGRAFIK menjadi "RENTANG.UMUR" dan "JENIS.KELAMIN"
penduduk.dki.transform[c("RENTANG.UMUR","JENIS.KELAMIN")] <- colsplit(penduduk.dki.transform$DEMOGRAFIK,"\\.",c("RENTANG.UMUR", "JENIS.KELAMIN"))

penduduk.dki.transform$DEMOGRAFIK <- NULL

penduduk.dki.transform
