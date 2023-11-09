sayilar=[12,3,19,6,7,23]

#sayilari ekrana yazdır:
'''i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1'''

#başlangıç ve bitiş sayılarini kullanicidan alip, aradaki tek sayilari ekrana yazdir:
'''baslangic=int(input('baslangic değerini girin:'))
bitis=int(input('bitis değerini girin:'))

while baslangic<bitis:
    baslangic+=1
    if baslangic%2:
     print(baslangic)'''

#1-100 arasındaki sayilari azalan şekilde sıralayın:
'''i=100
while i>0:
    print(i)
    i-=1'''

#kullanıcıdan aldığınız 5 sayıyı sıralı bir şekilde yazdirin:
'''sayilar=[]
i=0
while i<5:
    sayi=(int(input('sayi girin:')))
    sayilar.append(sayi)
    i+=1
print(sayilar)
sayilar.sort()
print(sayilar)'''

#bir urunler listesi olup, bu listeye kullanıcıdan kaç urun eklemek istediğini soran 
#ve bu urunleri de kullanıcıdan alan sonrasında da ürünleri ekrana yazdıran kodu yazın:
products=[]
number=int(input('Kaç Tane Urun Eklemek İstiyorsunuz?: '))
i=0
while i<number:
    name=input('Ürün Adini Giriniz:')
    price=int(input('Ürünün Fiyatını Giriniz:'))
    products.append({
        'name': name,
        'price': price
        })
    i+=1
    
for product in products:
    print(f"Ürün Adı: {product['name']} Ürün Fiyatı: {product['price']}")


    