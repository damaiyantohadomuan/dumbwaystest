# created by damaiyanto hadomuan
# username, hanya boleh huruf kecil dan terdiri dari 8 karakter, selain itu invalid
# email, hanya valid ketika mengandung char '@' dan hanya boleh huruf kecil
#jawaban nomor 2

def cekhurufkecil(text):
    counter=0
    hurufkecil="abcdefghijklmnopqrstuvwxyz@."
    panjangtext=len(text)
    for cekhuruf1 in range (0,panjangtext):
        for cekhuruf2 in range(0,27):
            if(text[cekhuruf1]==hurufkecil[cekhuruf2]):
                counter=counter+1
    if counter==panjangtext:
        return True
    else:
        return False

def Cekemail(text):
    #cek ada @ atau tidak
    panjangtext=len(text)
    cekAD= False #default @ tidak ada
    for cek in range (0,panjangtext):
        if text[cek] =='@' :
            cekAD =True #nilai diubah ke TRUE jika ada @

    #pemisahantextbaru
    #hurufkecil="abcdefghijklmnopqrstuvwxyz"
    textbaru=[]

    #simpandulu
    for cek1 in range (0,panjangtext):
        if text[cek1]!= '@' and text[cek1]!= '.':
            textbaru.append(text[cek1])
    textbaruu="".join(textbaru)

    #cek text huruf kecil atau tidak
    hasil=cekhurufkecil(textbaruu)
    if(cekAD==True and hasil==True):
        return True
    else:
        return False

def cekjumlahkarakter(text):
    if(len(text)==8):
        return True
    else:
        return False

def validationusername(username):
    #cek username dan email
    if (cekhurufkecil(username)==True) and (cekjumlahkarakter(username)==True): #and (Cekemail(email)==True):
        print("status : valid")
    else:
        print("status : tidak valid")

def validationemail(email):
    #cek username dan email
    if Cekemail(email)==True:
        print("status : valid")
    else:
        print("status : tidak valid")

username = input("username: ")
validationusername(username)
email = input("email: ")
validationemail(email)

