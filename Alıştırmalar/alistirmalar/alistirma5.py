#1
# sayi = input("altı basamaklı bir sayı giriniz: ")
# def sansli_sayi(sayi):
#     if int(sayi)<100000 or int(sayi)>999999:
#         raise ValueError("Hata: Lütfen 6 basamaklı bir sayı giriniz")
#     else:
#         ilk_uc_basamak = int(sayi[0])+int(sayi[1])+int(sayi[2])
#         son_uc_basamak = int(sayi[3])+int(sayi[4])+int(sayi[5])
#         if ilk_uc_basamak == son_uc_basamak:
#             print("Bu bir şanslı sayıdır.")
#         else:
#             print("Bu bir şanslı sayı değildir.")
# try:
#     sansli_sayi(sayi)
# except ValueError as a:
#     print(a)

#2
# sayi = input("altı basamaklı bir sayı giriniz: ")
# def basamak_degistir(sayi):
#     if int(sayi)<100000 or int(sayi)>999999:
#         raise ValueError("Hata: Lütfen 6 basamaklı bir sayı giriniz")
#     else:
#         sayilar = list(sayi)
#         temp = sayilar[1]
#         sayilar[1] = sayilar[4]
#         sayilar[4] = temp

#     yeni_sayi= "".join(sayilar)
#     return yeni_sayi

# try:
#     sonuc = basamak_degistir(sayi)
#     print("Yeni sayı: ",sonuc)
# except ValueError as a:
#     print(a)

#3
ay = int(input("Lütfen bir ay numarasını giriniz: "))
def mevsimler(ay):
    if ay<1 or ay>12:
        raise ValueError("Hata: Geçersiz sayı.")
    elif ay== 1 or ay==2 or ay==12:
        print( "Winter")
    elif ay>=3 and ay<=5 :
        print("Spring")
    elif ay>=6 and ay<=8:
        print("Summer")
    else:
        print("Autumn")


try:
    mevsimler(ay)
except ValueError as e:
    e