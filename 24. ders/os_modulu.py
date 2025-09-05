import os

# print(dir(os))

# getcwd() Mevcut çalışma dizinini döner
# print(os.getcwd())

# chdir() Çalışma dizinini değiştirir
# print(os.getcwd())
# os.chdir("C:\\Users\\birgu\\OneDrive\\Desktop")  #'\' yerine '/' veya '\\' kullanmalıyız
# print(os.getcwd())

# listdir() Verilen dizindeki dosya/klasörleri listeler
# os.chdir("C:\\Users\\birgu\\OneDrive\\Desktop")
# print("Bulunduğumuz adres: ",os.getcwd())
# print(os.listdir())

# mkdir() Yeni klasör oluşturur
# os.mkdir("birgül_deneme")

#makedirs() İç içe klasörler oluşturur
# os.makedirs("birinci/ikinci/üçüncü")

#rmdir() Boş klasörü siler
# os.rmdir("deneme")

#removedirs() İç içe klasörleri siler
# os.makedirs("birinci/ikinci/üçüncü")
# os.removedirs("birinci/ikinci/üçüncü")

#rename() Dosya/klasör adı değiştirir
# os.rename("OOO","SSS")
# os.rmdir("SSS")
# os.rename("deneme.py","test.py")

#stat() dosya ya da klasör hakkında ayrıntılı bilgi verir
# print(os.stat("os_modulu.py"))

#walk() bir klasör ağacını (yani bir dizin ve alt dizinlerini) adım adım gezmek için kullanılır.
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("C:/Users/birgu/OneDrive/Desktop/repos/Alıştırmalar/"):
    print("Şu anki dizin: ",klasor_yolu)
    print("Klasörler: ",klasor_isimleri)
    print("Dosyalar: ",dosya_isimleri)
    print("**********************************")