def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    print(liste)
    isim = liste[0]
    vize1 = liste[1]
    vize2 = liste[2]
    final = liste[3]
    ortalama = int(vize1)*3/10 +int(vize2)*3/10+int(final)*4/10
    if ortalama >= 90 :
        harf = "AA"
    elif ortalama >=85:
        harf = "BA"
    elif ortalama >= 80:
        harf = "BB"
    elif ortalama>= 70:
        harf = "CB"
    elif ortalama>= 55:
        harf = "CC"
    else:
        harf = "FF"
    return isim + "------------"+ harf+ "\n"
with open("dosya.txt","r",encoding="utf-8") as file:
    liste = []
    for satir in file:
        liste.append(not_hesapla(satir))

with open("harf_notu.txt","w",encoding="utf-8") as file2:
    file2.writelines(liste)