# kalıtım - inheritance

# class Calisan():
#     def __init__(self,isim,soyisim,maas,departman):
#         print("Çalışan sınıfının init fonksiyonu çalıştı.")
#         self.isim = isim
#         self.soyisim = soyisim
#         self.maas = maas
#         self.departman = departman

#     def bilgileri_goster(self):
#         print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı.")
#         print(f"Ad: {self.isim}\nSoyad: {self.soyisim}\nMaaş: {self.maas}\nDepartman: {self.departman}")

#     def departman_degistir(self, yeni_departman):
#         print("Çalışan sınıfının departman değiştir fonksiyonu çalıştı.")
#         self.departman =yeni_departman


# class Yonetici(Calisan):
#     def zam_yap(self,zam_miktari):
#         print("Zam yapılıyor...")
#         self.maas += zam_miktari

# # object - instance - instantiate etmek - obje - nesne
# yonetici1 = Yonetici("Birgül","Demir",500000,"IK")

# yonetici1.bilgileri_goster()

# yonetici1.zam_yap(80000)

# yonetici1.bilgileri_goster()

# yonetici1.departman_degistir("Yazılım")

# yonetici1.bilgileri_goster()

# print(dir(Yonetici))

# # # overriding (iptal etme) - override etmek

class Calisan():
    def __init__(self,isim,soyisim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu çalıştı.")
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı.")
        print(f"Ad: {self.isim}\nSoyad: {self.soyisim}\nMaaş: {self.maas}\nDepartman: {self.departman}")

    def departman_degistir(self, yeni_departman):
        print("Çalışan sınıfının departman değiştir fonksiyonu çalıştı.")
        self.departman =yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, departman, sorumlu_kisi_sayisi):
        # overriding
        print("Yönetici fonksiyonunun init fonksiyonu çalıştı.")
        super().__init__(isim,soyisim,maas,departman)
        self.sorumlu_kisi_sayisi = sorumlu_kisi_sayisi

    def zam_yap(self,zam_miktari):
        print("Zam yapılıyor...")
        self.maas += zam_miktari

    def bilgileri_goster(self):
        #overriding
        print("Yönetici sınıfının bilgileri göster metodu calıştı.")
        print(f"Yönetici Ad: {self.isim}\nYönetici Soyad: {self.soyisim}\nMaaş: {self.maas}\nDepartman: {self.departman}")


# object - instance - instantiate etmek - obje - nesne
yonetici1 = Yonetici("Birgül","Demir",500000,"IK",10)

yonetici1.bilgileri_goster()