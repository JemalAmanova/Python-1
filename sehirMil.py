# İlleri ve uzaklıklarını bir sözlükte saklayalım
iller = {"Ankara": 664, "Tekirdağ": 120, "Bursa": 436}

# Uzaklıkları kilometreden mile dönüştüren bir fonksiyon
def km_to_mil(km):
    return km * 0.621371

# Kullanıcıdan mil cinsinden bir değer isteyelim
mil_limit = float(input("Bir sınır değeri (mil olarak) girin: "))

# Uzaklıkları mile dönüştürelim
mil = map(km_to_mil, iller.values())

# Sınır değerinden büyük olan illeri filtreleyelim
uzak_iller = filter(lambda x: x > mil_limit, mil)

# Sonuçları ekrana yazdıralım
#zip() fonksiyonu, iki veya daha fazla koleksiyonu eşleştirip her bir koleksiyondan sırayla öğeler almanızı sağlar. İlk parametre olarak kullanılan koleksiyonun ilk öğesi, ikinci parametre olarak kullanılan koleksiyonun ilk öğesiyle eşleştirilir, ardından ikinci öğeler eşleştirilir ve bu işlem her iki koleksiyon için sona erer. Eşleştirilen öğeler bir demet (tuple) içinde bulunur.
for il, mil in zip(iller.keys(), uzak_iller):
    print(f"{il}: {mil:.2f} mil")






