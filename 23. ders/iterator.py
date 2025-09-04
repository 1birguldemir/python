# iterator - iterable object

#bir objenin itarable olabilmesi için __iter__() ve __next__() metodlarını tanımlamamız gerekir

# liste = [1,2,3,4,5]

# # print(dir(liste))

# iterator = iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)

# liste = [1,2,3,4,5]

# iterator = iter(liste)

# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break

# __iter__() - __next__()

class Kumanda:
    def __init__(self,kanal_listesi):
        self.kanallar = kanal_listesi
        self.index = -1 

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index < len(self.kanallar):
            return self.kanallar[self.index]
        else:
            self.index = -1
            raise StopIteration
        
kumanda1 = Kumanda(["TRT1","FOX","STAR","NTV","SHOW"])
iterator =iter(kumanda1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
