import time 

# def kareleri_hesapla(sayilar):
#     basla = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i**2)

#     print("Kareleri hesapla fonksiyonu bitti.")
#     bitis = time.time()
#     print(f"bu işlem {bitis-basla} saniye sürdü.")

# def küpleri_hesapla(sayilar):
#     basla = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i**3)

#     print("Küpleri hesapla fonksiyonu bitti.")
#     bitis = time.time()
#     print(f"bu işlem {bitis-basla} saniye sürdü.")

# kareleri_hesapla(range(100000000))
# küpleri_hesapla(range(10000000))

def sure_hesapla(fonksiyon):
    def wrapper(sayilar):
        basla = time.time()
        sonuc = fonksiyon(sayilar)
        bitis = time.time()
        print(fonksiyon.__name__+" fonksiyonu "+str(bitis-basla)+" saniye sürdü.")
        return sonuc
    return wrapper

@sure_hesapla
def kareleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i**2)
    print("Kareleri hesapla fonksiyonu bitti.")

@sure_hesapla
def küpleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i**3)
    print("Küpleri hesapla fonksiyonu bitti.")

kareleri_hesapla(range(100000))
küpleri_hesapla(range(100000))