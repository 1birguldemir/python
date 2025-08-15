import math
import modul1

def hesap_makinesi():
    print("""
        Gelişmiş Hesap Makinesi - Math Modülü İle
        1. Karekök alma
        2. Üs alma
        3. Sinüs hesaplama
        4. Kosinüs hesaplama
        5. 10 tabanında logaritma hesaplama
        6. Kendi faktöriyel fonksiyonunu çalıştır
        7. Kendi üs alma fonksiyonunu çalıştır
        8. kendi karekök alma fonksiyonunu çalıştır.
        """)
    secim = input("Lütfen bir işlem seçiniz (1-5) :")
    if secim == "1" :
        sayi = int(input("Karekökünü almak istediğiniz sayı: "))
        print("Bu sayının karekökü :",math.sqrt(sayi))
    elif secim == "2":
        taban = int(input("Taban: "))
        üs = int(input("Üs: "))
        print("Üs hesaplamasının sonucu: ",math.pow(taban,üs))
    elif secim == "3":
        sin = int(input("hesaplanmasını istediğiniz sinüs değeri: "))
        print("Sinüs işleminin sonucu: ",math.sin(sin))
    elif secim == "4":
        cos = int(input("hesaplanmasını istediğiniz cosinüs değeri: "))
        print("Cosinüs işleminin sonucu: ",math.cos(cos))
    elif secim == "5":
        log = int(input("hesaplanmasını istediğiniz logaritma değeri: "))
        print("Logaritma işleminin sonucu: ",math.log10(log))
    elif secim == "6":
        sayi = int(input("Faktöriyel hesabı için bir sayı giriniz."))
        print(modul1.factorial(sayi))
    elif secim == "7":
        us = int(input("Üs: "))
        taban = int(input("taban: "))
        print(modul1.us_alma(taban,us))
    elif secim == "8":
        kok = int(input("Kökü alınacak sayıyı giriniz.: "))
        print(modul1.kok_alma(kok))
    else:
        print("Geçersiz işlem!")

while True:
    devam_mi = input("Yeni bir işlem yapmak ister misiniz? (e/h): ")
    if devam_mi == "e":
        hesap_makinesi()
    else:
        break