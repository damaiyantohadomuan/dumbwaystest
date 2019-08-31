# created by damaiyanto hadomuan
# Clue: Jika function dijalankan
# betweenDays('2018-11-01', '2018-11-05')
# akan diperoleh hasil:
# '2018-11-01', '2018-11-02', '2018-11-03', '2018-11-04', '2018-11-05'
#jawaban nomor 3



Jumlahhari= [31,28,31,30,31,30,31,31,30,31,30,31]
tanggal1=0
tanggal2=0
bulan1=0
bulan2=0
tahun1=0
tahun2=0

def inputan(tanggal,bulan,tahun):
    tanggal = int(input("tanggal: "))
    bulan   = int(input ("bulan : "))
    tahun   = int(input ("tahun : "))
    if (checkvalidation(tanggal,bulan,tahun)==True):
        return True,tanggal,bulan,tahun
    else:
        return False,tanggal,bulan,tahun

def checkvalidation(tanggal,bulan,tahun):#untuk mengecek apakah benar jumlah hari pada bulan tersebut
    if((Jumlahhari[bulan-1]>=tanggal) and (tahun!=0) and 0<=bulan<=12):
        return True
    else:
        return False

#============== MAIN PROGRAM ===================
print("===tanggal pertama===")
result=inputan(tanggal1,bulan1,tahun1)
while (result[0]==False):
    print("tanggal/bulan/tahun tidak valid, ulangi kembali")
    print("===tanggal pertama===")
    result=inputan(tanggal1,bulan1,tahun1)
tanggal1=result[1]
bulan1=result[2]
tahun1=result[3]

print("===tanggal kedua===")
result=inputan(tanggal2,bulan2,tahun2)
while (result[0]==False):
    print("tanggal/bulan/tahun tidak valid, ulangi kembali")
    print("===tanggal kedua===")
    result=inputan(tanggal2,bulan2,tahun2)
tanggal2=result[1]
bulan2=result[2]
tahun2=result[3]

for counter in range(tanggal1,tanggal2+1):
    print(tahun1,"-",bulan1,"-",counter)




