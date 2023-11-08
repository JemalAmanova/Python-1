import math

def fonksiyonhipo(x, y):
    h = math.sqrt((x**2 + y**2))
    return h

def fonksiyonkenar(x,h):
    y =math.sqrt((h**2 - x**2))
    return y



deger=input("Dikucgenin kenarlarini önce kisa kenarlar sonra hipotenus seklinde giriniz")
dizi=deger.split(",")
if dizi[2]=="?":
 print(fonksiyonhipo(int(dizi[0]), int(dizi[1])))
elif dizi[0]=="?":
    print(fonksiyonkenar(int(dizi[1]), int(dizi[2])))
elif dizi[1]=="?":
    print(fonksiyonkenar(int(dizi[0]), int(dizi[2])))
else:
    print("Lütfen Dikucgenin kenarlarini önce kisa kenarlar sonra hipotenus seklinde giriniz")
    




