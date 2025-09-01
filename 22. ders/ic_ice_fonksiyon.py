# def fonksiyon(isim,*args):
#     print("İsim: ",isim)
#     print(args)
#     print("args elemanları: ")
#     for i in args:
#         print(i)

# fonksiyon("birgül",1,2,3,4,5,6,7,8,9)

# def yeni_fonksiyon(*args,**kwargs):
#     for i in args:
#         print("Argümanlar: ",i)
#     print("****************************")
#     for key,value in kwargs.items():
#         print(f"Argüman ismi: {key} - Argüman değeri: {value}")

# yeni_fonksiyon(1,2,3,4,5,"birgül","demir",isim = "osman" , soyisim = "demir" , yaş = 12)

# def selamla(isim):
#     print("Selam ",isim)
# # selamla("Faruk")

# degisken_ismi = selamla
# # print(degisken_ismi)
# # degisken_ismi("Tyfun")
# # selamla("Zeynep")

# del selamla
# # selamla("Zeki")
# degisken_ismi("Müjdat")


#scope1
# def fonksiyon():
#     #scope2
#     def fonksiyon2():
#         print("Ben küçük bir fonksiyonum.")
#     print("Ben büyük bir fonksiyonum.")
#     fonksiyon2()
# fonksiyon()
# fonksiyon2() #çağırılamaz sadece scope 2 de çağırılabilir.

# def fonksiyon(*args):
#     def topla(args):
#         toplam =0
#         for i in args:
#             toplam += i
#         return toplam
#     # print(topla(args))
# fonksiyon(1,2,3,4,5,6,7)

# def fonksiyon(islem_adi):
#     def topla(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
#     def carp(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim
    
#     if islem_adi == "topla":
#         return topla
#     else:
#         return carp
    

# print(fonksiyon("carp")(1,2,3,4,5))

# def toplama(a,b):
#     return a+b
# def carpma(a,b):
#     return a*b
# def cikarma(a,b):
#     return a-b
# def bolme(a,b):
#     return a/b 

# def anafonksiyon(func1,func2,func3,func4,islem_adi):
#     if islem_adi == "toplama":
#         print(func1(5,10))
#     elif islem_adi == "carpma":
#         print(func2(5,10))
#     elif islem_adi == "cikarma":
#         print(func3(5,10))
#     elif islem_adi == "bolme":
#         print(func4(5,10))
#     else:
#         print("Geçersiz işlem...")

# anafonksiyon(toplama,carpma,cikarma,bolme,"bolme")