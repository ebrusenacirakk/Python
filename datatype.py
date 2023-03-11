#Odev 1
#VERİ TİPLERİ

#ınt : Tam sayıların tutulduğu veri tipidir. Örneğin 3, 5, 99 vb.

#float : Ondalıklı sayıların tutulduğu veri tipidir. Örneğin 75.8, 99.3 vb.

#string : Metinsel ifadelerin (yazıların ve karakterlerin) tutulduğu veri tipidir. Çift veya tek tırnak ile 
#gösterilir. Örneğin "Sena"

#bool : Mantıksal bir veri tipidir. True ya da false değerler alır.

#Odev 2
#Kayıt ol ve Giriş ekranlarındaki "fullname" , "email" ve "password" alanları string veri tipine örnektir.
#Giriş yapıldıktan sonra kayıtlı olduğumuz kursların tamamlanma yüzdeleri int veri tipine örnektir.
#Kayıt ekranında "zaten bir hesabınız mı var" sorusu true dönüyorsa login ekranına yönlendiriyor. Bu bir bool tipine örnektir.
#Sıkça sorulan sorularda Canlı yayın saati alanı (21.00) string ya da float olarak tanımlanmış olabilir.

#Odev 3

hesabıvarmi = True

if hesabıvarmi == True:
    print("Giriş sayfasına yönlendir")

else:
    print("Mail adresine ait kullanıcı bulunamadı")

odev1 = "Tamamlandı mı?"
odev2 = "Tamamlandı mı?"
cevap1 = "evet"
cevap2 = "hayır"

if odev1 and odev2 == cevap1:
    print("Kursun 2. gününe geç")
elif odev1 and odev2 == cevap2:
    print("Ödevleri tamamlamadan 2. güne geçmeyin")
else:
    print("Ödevler tamamlanmadığında konuların pekişmesi zordur.")
#Bu kısmı tamamen uydurdum.





