import random

fenerbahce = []
galatasaray = []
besiktas = []
def takim(satir):
    parçalar = satir.split(",")
    isim = parçalar[0].strip()
    takim =parçalar[1].strip()
    
    if takim == "Fenerbahçe":
        fenerbahce.append(isim+ "\n")
    elif takim == "Beşiktaş":
        besiktas.append(isim+ "\n")
    elif takim == "Galatasaray":
        galatasaray.append(isim+ "\n")


with open("futbolcular.txt","r",encoding="utf-8") as file:
    futbolcular =file.readlines()
    random.shuffle(futbolcular)
    for satir in futbolcular:
        takim(satir)



with open("futbolcular.txt","w",encoding="utf-8") as file1:
    file1.writelines(futbolcular)

with open("fb.txt","w",encoding="utf-8") as file2:
    file2.writelines(fenerbahce)

with open("gs.txt","w",encoding="utf-8") as file3:
    file3.writelines(galatasaray)

with open("bjk.txt","w",encoding="utf-8") as file4:
    file4.writelines(besiktas)