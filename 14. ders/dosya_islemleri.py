# 'r' kipi/mode - read

# try:
#     dosya = open("bilgiler.txt","r",encoding="utf-8")
#     for satir in dosya:
#         print(satir,end="")
#     dosya.close()
# except:
#     print("Dosya bulunamadı.")

#dosya.close()

# try:
#     dosya = open("bilgiler.txt","r",encoding="utf-8")
#     #read() fonksiyonu 
#     icerik1 = dosya.read()
#     print("Dosyanın içeriği (1. dosya okuması): ")
#     print(icerik1)
#     icerik2 = dosya.read()
#     print("Dosyanın içeriği (2. dosya okuması): ")
#     print(icerik2)
#     dosya.close()
# except:
#     print("Dosya bulunamadı.")


# try:
#     dosya = open("bilgiler.txt","r",encoding="utf-8")
#     #readline() fonksiyonu
#     icerik1 = dosya.readline()
#     print("Dosyanın içeriği (1. dosya okuması):")
#     print(icerik1)
#     icerik2 = dosya.readline()
#     print("Dosya içeriği (2. dosya okuması):")
#     print(icerik2)
#     icerik3 = dosya.readline()
#     print("Dosyanın içeriği (3. dosya okuması):")
#     print(icerik3)
# except:
#     print("dosya bulunamadı...")


#readlines() fonksiyonu
file = open("Bilgiler.txt","r",encoding="utf-8")
icerik = file.readlines()
print("Readlines() fonksiyonu ile bastırıldı.")
print(icerik)