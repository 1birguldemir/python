#beden kitle indeksi hesaplama
# boy = float(input("boyunuzu giriniz:"))
# kilo = float(input("kilonuzu giriniz:"))
# index = kilo /(boy*boy)
# print("beden kitle indeksiniz: {:.2f}".format(index))
# if index<18.5:
#     print("zayıf")
# elif index>=18.5 and index<25:
#     print("normal")
# elif index>=25 and index<30 :
#     print("kilolu")
# else:
#     print("obez")

#en büyük sayıyı belirleme
# s1 = int(input("1. sayıyı giriniz: "))
# s2 = int(input("2. sayıyı giriniz: "))
# s3 = int(input("3. sayıyı giriniz: "))
# en_buyuk = s1
# if s1<s2:
#     en_buyuk = s2
# elif s3>s2 and s3>s1:
#     en_buyuk = s3

# print(en_buyuk)


#harf notu belirleme
# vize1 = int(input("1. vize notunuzu giriniz: "))
# vize2 = int(input("2. vize notunuzu giriniz: "))
# final = int(input("final notunuzu giriniz: "))
# toplam = vize1*0.3+ vize2*0.3+ final*0.4
# print(toplam)
# if toplam>=90: 
#     print("AA")
# elif toplam>=85:
#     print("BA")
# elif toplam>=80:
#     print("BB")
# elif toplam>=75:
#     print("CB")
# elif toplam>=70:
#     print("CC")
# elif toplam>=65:
#     print("DC")
# elif toplam>=60:
#     print("DD")
# elif toplam>=55:
#     print("FD")
# else:
#     print("FF")


şekil = input("üçgen mi dörtgen mi?")

if şekil == "üçgen":
    a = int(input("üçgenin birinci kenar uzunluğunu giriniz"))
    b = int(input("üçgenin ikinci kenar uzunluğunu giriniz"))
    c = int(input("üçgenin üçüncü kenar uzunluğunu giriniz"))
    if a==b==c:
        print("eşkenar üçgen")
    elif a==b or b==c or a==c :
        print("ikizkenar üçgen")
    elif abs(a-b)>c or abs(a-c)>b or abs(b-c)>a :
        print("üçgen belirtmiyor")
    else: 
        print("sıradan bir üçgen")
elif şekil == "dörtgen":
    a = int(input("dörtgenin birinci kenar uzunluğunu giriniz"))
    b = int(input("dörtgenin ikinci kenar uzunluğunu giriniz"))
    c = int(input("dörtgenin üçüncü kenar uzunluğunu giriniz"))
    d = int(input("dörtgenin dördüncü kenar uzunluğunu giriniz"))
    if a==b==c==d :
        print("kare")
    elif (a==c and b==d) or (a==b and c==d) :
        print("dikdörtgen")
    else:
        print("sıradan bir dörtgen.")
else:
    print("geçersiz işlem.")
