from datetime import datetime

# print(dir(datetime))

# now() 
# su_an = datetime.now()
# # print("Şu anki zaman: ",su_an)
# print("Şu anki yıl: ",su_an.year)
# print("Şu anki ay: ",su_an.month)
# print("Şu anki gün: ",su_an.day)
# print("Şu anki saat: ",su_an.hour)
# print("Şu anki dakika: ",su_an.minute)
# print("Şu anki saniye: ",su_an.second)
# print("Şu anki mikrosaniye: ",su_an.microsecond)

#ctime()
# print("Şu anki zaman güzelleştirilmiş görünümü: ",su_an.ctime())

# strftime()
        # Yıl bilgisini almak için: %Y

        # Ay ismini almak için: %B

        # Gün ismini almak için: %A

        # Saat bilgisini almak için: %X

        # Gün bilgisini almak için: %D
# suan = datetime.now()
# print(datetime.strftime(suan,"%Y"))
# print(datetime.strftime(suan,"%A"))
# print(datetime.strftime(suan,"%B"))
# print(datetime.strftime(suan,"%X"))
# print(datetime.strftime(suan,"%D"))
# print(datetime.strftime(suan,"%Y %X"))
# print(datetime.strftime(suan,"%Y %A %B"))
# import locale
# print(locale.setlocale(locale.LC_ALL,""))
# print(datetime.strftime(suan,"%Y %A %B"))

#timestamp() Bir datetime nesnesini → Unix zaman damgasına (timestamp) çevirir.
#fromtimestamp() Bir timestamp değerini → datetime nesnesine çevirir.
# suan = datetime.now()
# print(datetime.timestamp(suan))
# saniye = datetime.timestamp(suan)
# zaman = datetime.fromtimestamp(saniye)
# print("Şu anki zaman: ",zaman)

tarih = datetime(2023 ,12,21)
suan = datetime.now()
fark = suan- tarih
print("Aradaki tarih farkı: ",fark.seconds)