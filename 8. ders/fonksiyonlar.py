# gömülü fonksiyonlar - built-in functions
# user defined - kullanıcı tanımlı fonksiyonlar


# def selamla():
#     #fonction deninition
#     print("Selamlar arkadaşlar...")
#     print("Nasılsınız?")

# print(type(selamla))
# function calling

# selamla()
# selamla()
# selamla()
# selamla()
# selamla()


# def selamla(isim):
#     #fonction deninition
#     print("Selamlar ",isim)
#     print("Nasılsınız?")

# selamla("Birgül")


# def toplama(a,b,c):
#     print("sayıların toplamı: ",a+b+c)
# toplama(10,20,30)


# def faktoriyel(sayi):
#     faktoriyel=1
#     if sayi==0 or sayi == 1:
#         print("faktöriyel",faktoriyel)
#     else:
#         while sayi>=1:
#             faktoriyel *=  sayi
#             sayi -= 1
#         print("faktöriyel: ",faktoriyel)

# faktoriyel(345)

# def selamla(isim = "İsimsiz"):
#         #fonction deninition
#         print("Selamlar ",isim)
#         print("Nasılsınız?")

# selamla("Melih")


# def bilgileriGoster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara = "Bilgi Yok"):
#     print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

# bilgileriGoster(ad="Birgül",soyad="Demir",numara= 1552)

# print(1,2,3,sep=10)


#esnek sayıda değerler - yıldızlı parametreleri
def toplama(*parametreler):
    toplam = 0
    for i in parametreler:
        toplam += i
    print(toplam)

toplama(1,2,3,6)