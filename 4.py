# created by damaiyanto hadomuan
#function untuk menghitung jumlah jabat tangan yang terjadi dalam pertemuan yang dihadiri oleh beberapa orang.
# Jika setiap orang berjabat tangan dengan semua yang hadir dan hanya sekali berjabat tangan tangan dengan orang yang sama!
#jawaban nomor 4

def hitungjabattangan(panjang):
    counter=0
    for counter1 in range (1,(panjang+1)):
        for counter2 in range (1,(panjang+1)-counter1):
            counter=counter+1
    return counter
panjang = int(input("panjang: "))
counter=hitungjabattangan(panjang)
print(counter)
