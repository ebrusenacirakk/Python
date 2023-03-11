print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)

#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => tam sayı
ekVade = 6
vade = 36

#float, decimal, double
aylikOdeme = 200.50

#bool, boolean => True veya false
yukselisteMi = True

#Matematiksel Operatörler

#Toplama Operatörü
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

#Çıkarma Operatörü

print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

#Çarpma Operatörü

print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

#Bölme Operatörü

print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print (10 / 10)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# Mod Operatörü => %
print(10 % 2)
print (vade % 5)
print (30 % 10)

#Mantıksal Operatörler (çıktısı true ya da false değerini alıyor)

print(1 == 1)
print(1 == 2)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

#CTRL K + CTRL C hihglight ettikten sonra bu komutla çoklu yorum satırına alabilirsin

print(1 != 1)
print(1 != 2)

# or and (or en az bir true ifade arıyor, eğer varsa sonuç true dönüyor. And en az bir false değer arıyor, 
# eğer bir false değer varsa sonuç false dönüyor)

print(1 > 2 or 5 > 2 )
print(1 > 2 and 5 > 2 )
print(1 > 2 or 5 > 2 and 3 > 2)

#Karar yapıları
#if else

sayi1 = 10
sayi2 = 15
#sayi1 sayi2 den büyükse ekrana sayi 1 daha büyük yazdır

#indent (if kullanıldığında içine yazılacak sonuç 1 satır içeride olmalı, yoksa hata veriyor)
if sayi1 > sayi2:
    print("Sayi 1 sayi 2 den büyüktür")
    print("Hala if bloğunun içerisindeyim")
#eğer if bloğuna girmez ise 
elif sayi1 == sayi2:
    print("İki sayı eşittir")
else:
    print("Sayi 1 sayı 2 den küçüktür")
print("Burası if bloğunun dışıdır.")
