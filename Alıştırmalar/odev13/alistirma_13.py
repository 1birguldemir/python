#1
# class kareler:
#     def __init__(self,max=0):
#         self.max = max
#         self.sayi = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.sayi <= self.max:
#             sonuc = self.sayi ** 2
#             self.sayi += 1
#             return sonuc
#         else:
#             raise StopIteration


# kare = kareler(4)
# iteration = iter(kare)
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))

#2
def asal_sayilar():
    for sayi in range(2,1000):
        for i in range(2,sayi):
            if sayi % i ==0:
                break
        else:
            yield sayi

generator = asal_sayilar()
iterator = iter(generator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

