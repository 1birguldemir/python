# def kareleri_al():
#     sonuc = []
#     for i in range(1,6):
#         sonuc.append(i**2)
#     return sonuc

# print(kareleri_al())

# def kareleri_al():
#     # generator fonksiyon
#     for i in range(1,6):
#         yield i**2

# # print(kareleri_al())
# generator =kareleri_al()
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# liste = [i*3 for i in range(6)]
# print(liste)

# generator
# generator_liste = (i*3 for i in range(6))
# # print(generator_liste)
# iterator = iter(generator_liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# def carpim_tablosu():
#     # generator fonksiyonu
#     for i in range(1,11):
#         for j in range(1,11):
#             yield f"{i} x {j} = {i*j}"

# # for i in carpim_tablosu():
# #     print(i)

# generator = carpim_tablosu()
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for i in range(1,101):
#     print(i)

# generator = range(1,101)
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))