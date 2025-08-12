# def toplama(a,b,c):
#     print("toplama fonksiyonu")
#     return a+b+c

# def ikiyle_carp(sayi):
#     print("ikiyle çarp fonksiyonu")
#     return sayi*2

# toplam = toplama(1,2,3)
# print(ikiyle_carp(toplam))


def ucle_carp(sayi):
    print("üçle çarp fonksiyonu")
    return sayi*3

def ikiyle_topla(sayi):
    print("ikiyle toplama fonksiyonu")
    return sayi+2

def dorde_bol(sayi):
    print("dörde bölme fonksiyonu")
    return sayi/4

print(dorde_bol(ikiyle_topla(ucle_carp(5))))