from kutuphane import *

kutuphane = Kütüphane()

while True:
    print("""
      ********************************************
        Kütüphane programına hoşgeldiniz
        İşlemler:
        1.Kitapları göster
        2.Kitap sorgula
        3.Kitap ekle
        4.Kitap sil
        5.Baskı yükselt
        
        Çıkmak için 'q' ya basınız.

      ********************************************
""")
    islem = input("Yapacağınız işlem: ")
    if islem =="q":
        print("Çıkış yapılıyor...")
        break
    elif islem== "1":
        kutuphane.kitaplari_goster()
    elif islem== "2":
        isim = input("Hangi kitabı sorgulamak istiyorsunuz: ")
        print("Sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitaplari_sorgula(isim)
    elif islem == "3":
        isim = input("Kitap ismi: ")
        yazar = input("Kitabın yazarı: ")
        yayinevi = input("Kitabın yayın evi: ")
        tur = input("Kitabın türü: ")
        baski = input("Kitabın baskı sayısı: ")
        eklenecek_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(eklenecek_kitap)
        print("Kitap eklendi.")
    elif islem == "4":
        isim = input("Silmek istediğiniz kitabın ismini giriniz: ")
        soru = input("Silmek istediğinizden emin misiniz? (e/h)")
        if soru == "e":
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi.")
    elif islem == "5":
        isim = input("Baskı sayısını yükseltmek istediğiniz kitabın adını giriniz: ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_artir(isim)
        print("Baskı yükseltildi.")
    else:
        print("Geçersiz işlem...")