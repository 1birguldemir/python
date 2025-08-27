#1
# str = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
# for i in str:
#     print(f"{i}: {str.count(i)}" )

#1 başka yöntem
# text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# print(frequency)


#2
# with open("şiir.txt","r",encoding="utf-8") as file:
#     for liste in file:
#         print(liste[0],end="")

#2 başka yöntem
# with open("şiir.txt", "r", encoding="utf-8") as file:
#     first_letter = []
#     for text in file:
#         text = text.lstrip()
#         if text:
#             first_letter.append(text[0])

# sonuc = "".join(first_letter)
# print(sonuc)

#3
with open("mailler.txt","r",encoding="utf-8") as file:
    liste = file.readlines()
    def format(satir):
        if "@" in satir:
            indeks1 = satir.find("@")
            if "." in satir[indeks1:]:
                indeks2 = satir.find(".",indeks1)
                uzunluk = len(satir)
                if uzunluk - indeks2-1 >= 2:
                    print(satir)

for satir in liste:
    format(satir)

    # proje 3 - mail formatı kontrol etme , başka çözüm
with open("mailler.txt", "r", encoding="utf-8") as file:
    for text in file:
        text = text.strip()
        if (
            text.count("@") == 1
            and " " not in text
            and text.find("@") > 0
            and "." in text.split("@")[1]
            and "xyz" not in text
            and text.lower() in text
        ):
            print(text)

#4
isimler = ["Kerim","Tarık","Ezgi","Kemal","Ilkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste = list(zip(isimler,soyisimler))
liste.sort()
print(liste)