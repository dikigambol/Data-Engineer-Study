data_intro <- read.csv("https://storage.googleapis.com/dqlab-dataset/data_intro.csv", sep=";")

## analisis bagaimana hubungan pendapatan dengan total belanja mengunakan scatter plot
plot(data_intro$Pendapatan, data_intro$Total)
