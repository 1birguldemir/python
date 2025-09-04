def extra(func):
    def wrapper(sayilar):
        cift_toplami = 0
        cift_sayilar = 0
        tek_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if sayi % 2 == 0:
                cift_toplami += sayi
                cift_sayilar +=1
            else:
                tek_toplami += sayi
                tek_sayilar += 1
        print("Çift sayıların ortalaması: ",cift_toplami/cift_sayilar)
        print("Tek sayıların ortalaması: ",tek_toplami/tek_sayilar)
        func(sayilar)
    return wrapper

@extra
def ortalama_bul(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi 
    print("Sayıların ortalaması: ",toplam/len(sayilar))

ortalama_bul([1,2,3,4,5,6,7,8])