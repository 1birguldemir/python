#2 

def muk_sayilar(fonksiyon):
    def wrapper():
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            while i < sayi:
                if sayi % i == 0:
                    toplam += i
                i += 1
            if toplam == sayi:
                print(sayi)
        fonksiyon()
    return wrapper


@muk_sayilar
def asal_sayi():
    for sayi in range(2,1001):
        i = 2
        while i<sayi:
            if sayi % i ==0:
                break
            i += 1
        else:
            print(sayi)

asal_sayi()