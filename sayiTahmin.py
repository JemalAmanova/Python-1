import random

print("SAYI TAHMİN OYUNUNA HOŞ GELDİNİZ")

#puan hesaplayan fonksiyon
def puanlama (x,y):
    puan=100-(100/x)*(y-1)
    return puan

#rastgele sayi oluşturalim 1 ve 10 arası:
sayi=random.randint(1,10)

#hak sayısını kullanicidan alalim
hak=int(input("kaç tahmin hakkı istiyorsunuz?:"))
tahminSayaci=0


while hak>0:
    hak-=1
    tahminSayaci+=1
    tahmin=int(input("tahmininizi girin:"))
    
        
    if tahmin==sayi:
        print(f"tebrikler {tahminSayaci} . tahmininizde bildiniz puanınız{100-(100/hak)*(tahminSayaci-1)}")
        break
    elif tahmin<sayi:
        print("daha büyük tahmin yapın")
    else:
        print("daha küçük tahmin yapın")
    if hak==0:
        print(f"Üzgünüz Hakkiniz Bitti. Tutulan Sayi: {sayi}")
        
    
