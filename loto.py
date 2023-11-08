import random
import re
import os

tahminler=[]

dogruTahminler=[]
sayilar=[]
kolonK=1
kolonR=1
kolonSayisi=int(input("kolon sayisi girin:"))

while kolonK<=kolonSayisi:
    tahmin=int(input("1 ile 49 arasında bir Sayi Tahmininizi giriniz"))
    if 0<tahmin<=49:
        tahminler.append(tahmin)
        kolonK+=1
    else:
        print("Lütfen 1 ile 49 arasinda sayi giriniz:")
print("Girdiginiz sayilar : ")
print(tahminler)
        
while kolonR<=kolonSayisi:
    sayi=random.randint(1,49)
    sayilar.append(sayi)
    kolonR+=1
print("Rastgele Sayilar : ")
print(sayilar)

for t in tahminler:
    for s in sayilar:
        if t==s:
         dogruTahminler.append(t)
         print("Tebrikler! tutturdugunuz saylar:")
         print(dogruTahminler)
        else:
            pass
print("hic sayi tutturamadiniz")
    
        
        
    

       
    


