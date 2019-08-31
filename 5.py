# created by damaiyanto hadomuan
#function untuk mencetak garis miring dari karakter “ * ”, dengan parameter panjang kolom
#jawaban nomor 5

array=[]

def drawLine(panjang):
    for counter in range(0,panjang):
        array.append(" ")

    for baris in range(0,panjang):
        array[baris]="*"
        print("".join(array))
        array[baris]=" "


#==========MAIN===========
panjang= int(input("panjang: "))
drawLine(panjang)
