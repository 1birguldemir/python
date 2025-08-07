# 3 sayının çarpımı
s1 = int(input("1. sayıyı giriniz:"))
s2 = int(input("2. sayıyı giriniz:"))
s3 = int(input("3. sayıyı giriniz:"))
print("{}*{}*{}={}".format(s1,s2,s3,s1*s2*s3))


#beden kitle indeksi bulma
boy = float(input("lütfen boy ölçünüzü giriniz:"))
kilo = float(input("lütfen kilo ölçünüzü giriniz:"))
index = kilo/(boy*boy)
print("Beden kitle indeksiniz: {:.2f}".format(index))


#sürücünün ödemesi gereken tutar
yakıt = float(input("Aracınızın kilometrede ne kadar yaktığını giriniz: "))
km = float(input("Kaç km yol aldığınızı giriniz: "))
tutar = yakıt*km
print("Ödemeniz gereken tutar: {:.2f}".format(tutar))


#kullanıcı bilgisi
ad = input("AD:")
soyad = input("SOYAD:")
numara = input("NUMARA:")
print(ad,soyad,numara,sep="\n")


#sayıların yerlerini değiştirme
s1 = int(input("1. sayıyı giriniz:"))
s2 = int(input("2. sayıyı giriniz:"))
s1,s2=s2,s1
print("1.sayı:",s1)
print("2. sayı: ",s2)


#hipotenüs hesaplama
a= int(input("Dik üçgenin 1. kenar uzunluğunu giriniz:"))
b = int(input("Dik üçgenin 2. kenar uzunluğunu giriniz:"))
hipotenus = (a**2) + (b**2)
print("Hipotenus uzunluğu: ",hipotenus**0.5)