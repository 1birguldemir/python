# all - any

# def hepsi(liste):
#     # bütün değerler true ise true,en az bir tanesi false ise false döndürmek istiyoruz.
#     # liste= [True,True,True,False]
#     # return False
#     for i in liste:
#         if not i:
#             return False
#     return True

# # Boolean - True-False (sayısal) 1=True 0 =False
# # ınteger değerlerde 0 hariç tüm değerlerin boolean karşılığı True'dur.Sadece 0 ın değeri False'tur.

# # print(hepsi([1,2,3,4,5,6,7,8,9,0]))


# def herhangi(liste):
#     for i in liste :
#         if i:
#             return True
#     return False

# print(herhangi([False,False,False,False]))


# liste = [True,True,True,False]

# print(all(liste))

# print(any(liste))


#ENUMERATE FONKSİYONU

# liste = ["elma","armut","muz","kiraz"]
# sonuc = [(0,"elma"),(1,"armut"),(2,"muz"),(3,"kiraz")]
# sonuc = list()
# i=0
# for eleman in liste:
#     sonuc.append((i,eleman))
#     i+=1
# print(sonuc)

# sonuc = list(enumerate(liste))
# print(sonuc)

# liste = ["a","b","c","d","e","f","g"]
# for index,eleman in enumerate(liste):
#     if index % 2 == 0:
#         print(f"Index: {index} - Eleman: {eleman}")

#Filter()

#filter(mantıksal değer dönen bir tane fonksiyon(true-false),liste gibi tuple gibi iterable bir veritipi)
# sonuc = filter(lambda x: x% 2==0,range(0,1000))
# print(list(sonuc))

# def asal_mi(sayi):
#     i = 2 
#     if sayi <= 1:
#         return False
#     elif sayi == 1 :
#         return False
#     elif sayi == 2:
#         return True
#     else:
#         while i<sayi:
#             if sayi % i ==0:
#                 return False
#             i += 1
#             return True

# asal_sayilar = list(filter(asal_mi,range(0,1000)))
# print(asal_sayilar)

#map fonksiyonu 

# def double(sayi):
#     return sayi * 2

# print(tuple(map(double,(1,2,3,4,5,6,7))))

# print(tuple(map(lambda sayi: sayi**2,(1,2,3,4,5,6,7))))

# liste1 = [1,2,3,4]
# liste2 = [5,6,7,8]
# liste3 = [9,10,11,12]

# print(list(map(lambda sayi1,sayi2,sayi3: sayi1*sayi2*sayi3 , liste1,liste2,liste3)))

# from math import factorial

# print(list(map(factorial,(1,2,3,4,5,6,7))))

# def okunus(sayi):
#     if sayi == 1:
#         return "Bir"
#     elif sayi == 2:
#         return "İki"
#     elif sayi == 3:
#         return "Üç"
    
# print(list(map(okunus,(1,2,3))))

#zip()

# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10,11]

#sonuc = [(1,6),(2,7),(3,8),(4,9),(5,10)]

# i=0
# sonuc = list()
# while i<len(liste1) and i <len(liste2):
#     sonuc.append((liste1[i],liste2[i]))
#     i += 1
# print(sonuc)

# print(list(zip(liste1,liste2)))

# liste1 = [1,2,3,4,5]
# liste2 = [6,7,8,9,10,11]
# liste3 = ["Python","Java","C#","Javascript","C"]

# print(list(zip(liste1,liste2,liste3)))

# for i,j,k in zip (liste1,liste2,liste3):
#     print("i: ",i*2,"j: ",j/3,"k: ",k+" dili.")

# sozluk1 = {"Elma": 1,"Armut":2,"Kiraz":3}
# sozluk2 = {"Kalem":10,"Silgi":20,"Defter":30}

# print(list(zip(sozluk1,sozluk2)))
# print(list(zip(sozluk1.values(),sozluk2.values())))

#reduce()
from functools import reduce

# def toplama(sayi1,sayi2):
#     return sayi1+sayi2

# print(reduce(toplama,[12,18,20,10]))

# def maksimum(x,y):
#     if x>y:
#         return x
#     else:
#         return y
    
# print(reduce(maksimum,[78,-98,105,76,35,2,500]))

print(min([1,2,3,4,5,6,66,777,104,-87]))