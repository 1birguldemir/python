import math

# mükemmel sayı bulma fonk
# def muk_sayi(sayi):
#     toplam = 0
#     i=1
#     while i < sayi:
#         if sayi % i == 0 :
#             toplam += i
#         i+=1
#     return toplam == sayi

# liste = []
# for num in range(1,1001):
#     if muk_sayi(num):
#         print(num)


#ebob bulma
# num1 = int(input("Please enter first number: "))
# num2 = int(input("Please enter second number: "))

# def ebob(a,b):
#     temp =1
#     result = 1
#     while temp<=a and temp<=b:
#         if a%temp == 0 and b%temp==0:
#             result = temp
#         temp +=1
#     return result

# print(ebob(num1,num2))


#ekok bulma
# num1 = int(input("Please enter first number: "))
# num2 = int(input("Please enter second number: "))

# def ekok(a,b):
#     temp = max(a,b)
#     result =1
#     while temp>=a or temp>=b:

#         if temp % a == 0 and temp%b ==0:
#             result = temp
#             break
#         temp += 1
#     return result
# print(ekok(num1,num2))


#iki basamaklı sayının okunuşunu bulma
# num = int(input("Lütfen iki basamaklı bir sayı giriniz: "))
# def read_num(a):
#     tens = a // 10
#     nums1= {1:"On",2:"Yirmi",3:"Otuz",4:"Kırk",5:"Elli",6:"Altmış",7:"Yetmiş",8:"Seksen",9:"Doksan"}
#     units = a % 10
#     nums2 ={0:"",1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
#     read = nums1[tens]+" "+nums2[units]
#     return read
# print(read_num(num))


#pisagor
liste = list()
def pisagor_ucgeni():
    for a in range(1,101):
        for b in range(1,101):
            c2 = a*a +b*b
            c = math.isqrt(c2)
            if c*c == c2:               
                liste.append((a,b,c))
    return liste

print(pisagor_ucgeni())