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

def asal_mi(sayi):
    i = 2 
    if sayi <= 1:
        return False
    elif sayi == 1 :
        return False
    elif sayi == 2:
        return True
    else:
        while i<sayi:
            if sayi % i ==0:
                return False
            i += 1
            return True
        
asal_sayilar = list(filter(asal_mi,range(0,1000)))
print(asal_sayilar)