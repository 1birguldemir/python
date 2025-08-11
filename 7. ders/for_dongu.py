# print("a" in "ali ata bak.")


# print(4 in [1,2,3,4])


# print(100 in (10,20,30,40))


# liste = range(0,1000)
# toplam = 0
# for eleman in liste:
#     #her bir döngü adımına iterasyon denir.
#     if eleman %2 == 0:
#         toplam += eleman
# print("toplam: ",toplam)


# yazi = "Ayşe ılık süt iç."
# for karakter in yazi:
#     #iterasyon.
#     print(karakter*3 )


# demet = (1,2,3,4,5,6,7,8)

# for eleman in demet:
#     print("eleman: ",eleman)

# liste = [(1,2),(3,4),(5,6),(7,8)]

# for i,j in liste:
#     print("i:",i,"j:",j)


# liste = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
# for i,j,k in liste:
#     print("i:",i,"j:",j,"k:",k,"bu değerlerin toplamı= ",i+j+k)


sozluk = {"1":"Ocak","2":"Şubat","3":"Mart"}
#print(sozluk.keys())
# print(list(sozluk.values()))
# print(list(sozluk.items()))

# for eleman in sozluk.values():
#     print(eleman)

for eleman1,eleman2 in sozluk.items():
    print(eleman1 ,". ayın ismi: ",eleman2)