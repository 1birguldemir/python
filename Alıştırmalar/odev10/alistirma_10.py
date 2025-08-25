#1
# def alan(x,y):
#     return x*y

# print(list(map(lambda a:alan (a[0], a[1]),[(3,4),(10,3),(5,6),(1,9)])))

#2
from functools import reduce
# def cevre(x,y,z):
#     if abs(x-y)<z and z<x+y:
#         return True
#     return  False

# print(list(filter(lambda c:cevre(c[0],c[1],c[2]),[(3,4,5),(6,8,10),(3,10,7)])))

#3
# cift_sayilar = list(filter(lambda x : x%2 == 0,[1,2,3,4,5,6,7,8,9,10,11,12]))

# print(reduce(lambda x,y:x+y,cift_sayilar))

#4
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isimler,soyisimler))
for i in liste:
    print(i)