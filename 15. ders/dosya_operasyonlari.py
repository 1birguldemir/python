# w dosya kipi - write

# file = open("bilgiler.txt","w",encoding="utf-8")
# file.write("ayşe ılık süt iç.")
# file.close()

# a dosya kipi - append

# file = open("bilgiler.txt","a",encoding="utf-8")
# file.write("Ahmet koş Ahmet!\n")
# file.close()

#with deyimi - context manager

# with open("bilgiler.txt","r",encoding="utf-8") as file:
#     for i in file:
#         print(i)

# seek() fonksiyonu - tell() fonksiyonu

# with open("bilgiler.txt","r",encoding="utf-8") as file:
#     file.seek(5)  #dosyanın 5. baytına git. 5. karakter.
#     icerik = file.read(10) 
#     print(icerik)
#     print(file.tell())

# r+ kipi - hem okuma hem yazma

# with open("bilgiler.txt","r+",encoding="utf-8") as file:
#     print(file.read())
#     file.seek(11)
#     file.write("birgül demir")
    # file.seek(0)
    # print(file)


# with open("bilgiler.txt","r+",encoding="utf-8") as file:
#     icerik = file.read()
#     icerik = "Ahmet Dursun\nİlhan Mansız\n"+ icerik
#     file.seek(0)
#     file.write(icerik)


#dosya ortasına ekleme

with open("bilgiler.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(7,"Birsen\n")
    liste.insert(9,"Osman\n")
    file.seek(0)
    # for satir in liste:
    #     file.write(satir)
    file.writelines(liste)
    file.seek(0)
    icerik = file.read()
    print("içerik: ",icerik)