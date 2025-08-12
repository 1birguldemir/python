# scope - kapsam
#namespace - isim alanı

#local - yerel değişkenler

#global değişkenler


# a = 10 #global
# #scope 1
# b=20

# def my_func():
#     c= 30
#     #scope2
#     print(a)
#     def baska_func():
#         print(c)
#         #scope 3
#         print("selcuk")
#     baska_func()

# my_func()
# print(a)

# global deyimi 
# d = 10

# def my_func():
#     global d
#     d = 4
#     print(d)

# my_func()
# print(d)


#scope 1
if True:
    #scope 1
    t = 10
    print(t)

print(t)

# scope1 
while True:
    #scope1
    deger = 10
    print(deger)
    break
#scope1
print(deger)