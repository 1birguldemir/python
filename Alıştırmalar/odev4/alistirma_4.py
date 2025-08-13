# mükkemel sayı bulma
# sayi = int(input("Lütfen bir sayı giriniz: "))
# toplam = 0
# i =1
# while i<sayi:
#     if sayi % i == 0:        
#         toplam += i                            
#     i+=1
# print(toplam)
# if toplam == sayi:
#     print(sayi," bir mükemmel sayıdır.")
# else:
#     print(sayi," mükemmel sayı değildir.")


#armstrong sayı belirleme
# sayi = int(input("Lütfen bir sayı giriniz: "))
# bas_sayisi= len(str(sayi))
# toplam =0
# for i in str(sayi):
#     liste = int(i)
#     toplam += liste**bas_sayisi
# if toplam == sayi:
#     print(sayi," bir armstrong sayıdır.")
# else:
#     print(sayi," armstrong sayı değildir.")



#çarpım tablosu
# for i in range(1,11):
#     print("****************")
#     for j in range(1,11):
#         print(i,"x",j, " =",i*j)


#döngü sonlandırma
# toplam = 0
# while True:
#     sayi = (input("Lütfen bir sayı giriniz:"))
#     if sayi == "q":
#         break
#     toplam += int(sayi)
# print(toplam)


# 3'e bölünen sayılar
# liste = list(range(1,101))
# liste2 = list()
# for i in liste:
#     if i%3 != 0:
#         continue
#     else:
#         liste2.append(i)
# print(liste2)


#list comprehension ile çift sayıları yazdırma
liste = list(range(1,101))
cift_sayilar = [i for i in liste if i %2 ==0]
print(cift_sayilar)