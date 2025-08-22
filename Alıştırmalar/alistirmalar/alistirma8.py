import random
import time

#1
# sayi = int(input("Sayı girin: "))
# for i in range(1,11):
#     print(f"{sayi}x{i} = {sayi*i}")

#2
# while True:
#     islem = input("""
#         Yapmak istediğiniz işlemi seçiniz:
#         1. TL -> USD
#         2. TL -> EUR
#         3. USD -> TL
#         4. EUR -> TL
#         5. ÇIKIŞ
#     """)

#3
#     if islem == "5":
#         print("Çıkış yapılıyor...")
#         break
#     miktar = int(input("Bir miktar giriniz:"))
#     if islem == "1":
#         print(f"TL -> USD: {miktar/41:.2f}")
#     elif islem == "2":
#         print(f"TL -> EUR: {miktar/47:.2f}")
#     elif islem == "3":
#         print(f"USD -> TL: {miktar*41:.2f}")
#     elif islem == "4":
#         print(f"EUR -> TL: {miktar*47:.2f}")
#     else:
#         print("geçersiz işlem.")

#4
# alt = int(input("Aralığın en küçük değerini giriniz: "))
# ust = int(input("Aralığın en büyük değerini giriniz: "))
# while True:
#     sayi = int(input("Bir sayı giriniz: "))
#     if sayi<ust and sayi>alt:
#         for i in range(alt,ust+1):
#             if i != sayi:
#                 print(i,end=" ")
#             elif i == sayi:
#                 print(f"!{sayi}!",end=" ")

#5

sayi = random.randint(1,500)
start_time = time.time()
tahmin_sayisi = 0
while True:
    tahmin =(input("Tahmininizi giriniz (Çıkmak için 'q'): "))
    if tahmin == "q":
            print("Çıkış yapılıyor...")
            break
    elif sayi>int(tahmin):
        print("Daha büyük bir sayı giriniz.")
        tahmin_sayisi += 1
    elif sayi<int(tahmin):
        print("Daha küçük bir sayı giriniz.")
        tahmin_sayisi += 1
    elif sayi == int(tahmin):
        end_time = time.time()
        tahmin_sayisi += 1
        print(f"Tebrikler doğru tahmin ettiniz.\nSayı: {sayi}\nDeneme Sayısı: {tahmin_sayisi}\nGeçirilen süre: {end_time-start_time} ")