sayilar=[1,3,6,7,27,90,73]

#sayilar dizizsindeki hangi sayilkar 3'ün katıdır?
'''for sayi in sayilar:
    if sayi%3==0:
     print (sayi)'''
 
#listedeki sayilarin toplamı kaçtır?
'''toplam=0
for sayi in sayilar:
    toplam+=sayi
print(toplam)'''

#sayilar listesindeki tek sayilarinin karesini alın:
'''for sayi in sayilar:
    if sayi%2:
        print(sayi**2)'''

urunler=[{'name': 'telefon', 'price':6000},
      {'name': 'laptop', 'price':20000},
      {'name': 'kulaklık', 'price':700},
      {'name': 'TV', 'price':17000}
      ]

#urun listesindeki fiyatların toplamını yazın:
'''toplam=0
for urun in urunler:
    fiyat=int(urun['price'])
    toplam+=fiyat
print(toplam)'''

#urunlerden fiyatı 7000 üzeri urunleri yazdırın:
for urun in urunler:
   if urun['price']>7000:
       print(urun)

     