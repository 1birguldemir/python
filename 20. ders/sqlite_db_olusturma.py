import sqlite3
connection = sqlite3.connect("kütüphane.db")
cursor = connection.cursor()

# def tablo_olustur():
#     cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim text, yazar text, yayin_evi text,sayfa_sayisi int)")
#     connection.commit()

# tablo_olustur()

# def kayit_ekle(isim,yazar,yayin_evi,sayfa_sayisi):
#     cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayin_evi,sayfa_sayisi))
#     connection.commit()

# kayit_ekle("Küçük Prens","Charles Dickens","Everest",160)

# select()
# def verileri_al():
#     cursor.execute("SELECT * FROM kitaplik")
#     data = cursor.fetchall()
#     for i in data:
#         print(i)

# verileri_al()

# def verileri_al2():
#     cursor.execute("SELECT isim,yazar FROM kitaplik")
#     data = cursor.fetchall()
#     for i in data:
#         print(i)

# verileri_al2()

# def verileri_al3(yayinevi,sayfa_sayisi):
#     cursor.execute("SELECT * FROM kitaplik WHERE yayin_evi = ? AND sayfa_sayisi >=?",(yayinevi,sayfa_sayisi))
#     data = cursor.fetchall()
#     for i in data:
#         print(i)

# yayinevi = input("Aratmak istediğiniz yayın evini giriniz: ")
# sayfa_sayisi = input("Aratmak istediğiniz sayfa sayısını giriniz: ")
# verileri_al3(yayinevi,sayfa_sayisi)

# def verileri_guncelle(old_yayinevi,new_yayinevi):
#     cursor.execute("UPDATE kitaplik SET yayin_evi = ?,isim = 'editlendi' WHERE yayin_evi = ?",(new_yayinevi,old_yayinevi))
#     connection.commit()

# old_yayinevi = input("Değiştirmek istediğiniz yayın evinin adını giriniz: ")
# new_yayinevi = input("Hangi isimle değiştirmek istersiniz? ")
# verileri_guncelle(old_yayinevi,new_yayinevi)

def veri_sil(kitap_ismi,sayfa_sayisi):
    cursor.execute("DELETE FROM kitaplik WHERE isim = ? AND sayfa_sayisi = ? ",(kitap_ismi,sayfa_sayisi))
    connection.commit()
    print("İlgili kitap kütüphaneden silindi")

kitap_ismi = input("Lütfen silmek isteddiğiniz kitabın ismini giriniz: ")
sayfa_sayisi = input("Lütfen silmek isteddiğiniz kitabın sayfa sayısını giriniz: ")
veri_sil(kitap_ismi,sayfa_sayisi)
connection.close()