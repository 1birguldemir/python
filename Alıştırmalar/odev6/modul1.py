def factorial(sayi):
    faktoriyel = 1
    while sayi > 1:
        faktoriyel *= sayi
        sayi -= 1
    return faktoriyel


def us_alma(taban,us):
    sonuc = 1
    while us>0 :
        sonuc *= taban
        us -= 1
    return sonuc


def kok_alma(sayi):
    return sayi**0.5