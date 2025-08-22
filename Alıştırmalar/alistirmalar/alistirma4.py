#1
# sure = int(input("günün başlangıcından itibaren geçen süreyi saniye cinsinden giriniz."))
# kalan_sure = 24*3600 - sure
# saat = kalan_sure // 3600 
# dakika = (kalan_sure % 3600) // 60
# saniye = kalan_sure % 60
# print(f"{saat} saat {dakika} dakika {saniye} saniye")

#2
# secim = input("1. dairenin alanı\n2. dairenin çevresi")
# cap = int(input("dairenin çapını giriniz: "))
# if secim == "1":
#     print(3.14*cap*cap)
# elif secim == "2":
#     print(2*3.14*cap)

#3
# maaliyet = int(input("oyun konsolunun maliyetini giriniz: "))
# miktar = int(input("oyun konsolunun adedini giriniz: "))
# indirim_yuzdesi = int(input("İndirim yüzdesini giriniz."))
# indirimli_maaliyet = maaliyet-(maaliyet*indirim_yuzdesi/100)
# siparis_toplami = indirimli_maaliyet*miktar
# print("İndirimli maaliyet: ",indirimli_maaliyet)
# print("sipariş toplamı: ",siparis_toplami)

#4
# boyut = int(input("Dosyanın boyutunu giriniz (MB): "))
# hiz = int(input("dosyanın hızını giriniz (MB/s): "))
# inme_hizi = boyut/hiz
# saat = inme_hizi // 3600
# dakika = (inme_hizi % 3600) // 60
# saniye = inme_hizi % 60
# print(f"{saat} saat {dakika} dakika {saniye} saniyede indirilecektir.")

#5
# saat = int(input("Lütfen saati giriniz."))
# if saat>=0 and saat<6:
#     print("Good Night!")
# elif saat>=6 and saat<13:
#     print("Good Morning!")
# elif saat>=13 and saat<17:
#     print("Good Day!")
# elif saat>=17 and saat<24:
#     print("Good Evening!")