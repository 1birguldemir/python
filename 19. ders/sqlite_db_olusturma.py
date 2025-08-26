import sqlite3
connection = sqlite3.connect("kütüphane.db")
cursor = connection.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim text, yazar text, yayin_evi text,sayfa_sayisi int)")
    connection.commit()

tablo_olustur()

def kayit_ekle(isim,yazar,yayin_evi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayin_evi,sayfa_sayisi))
    connection.commit()

kayit_ekle("Sefiller","Victor Hugo","YK Yayınları",250)
connection.close()