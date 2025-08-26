# set - küme

# x = set() #boş küme
# print(type(x))

# liste = [1,2,3,4,5,3,3,2,5,6,7,2,3]
# print(liste)
# kume = set(liste)
# print(kume)

# kume = set("Python Programlama Dili.")
# print(kume)

# kume = {"Python","Php","Python","Javascript"}
# print(kume)

#sırasız bir veri tipidir.
# kume = {"Python","Php","Java","C#","C","Javascript"}
# print(kume)
# for i in kume:
#     print(i)

# kümede indexleme yok
# print(kume[0]) #ulaşamayız.

# kume = {"Python","Php","Java","C#","C","Javascript"}
# liste = list(kume)
# print(liste)
# print(liste[0])
# print(liste[1])

#add()
# kume = {1,2,3,4,5}
# kume.add(6)
# print(kume)

# iki kümenin farkı - difference()
# kume1 = {1,2,3,4,5,6}
# kume2 = {4,5,6,7,8,9}

# #kume1-kume2
# print(kume1.difference(kume2))

#difference_update()
# kume1 = {1,2,3,4,5,6}
# kume2 = {4,5,6,7,8,9}

# kume1.difference_update(kume2)
# print(kume1)

# discard()
# kume1 = {1,2,3,4,5,6}

# kume1.discard(3)
# kume1.discard(100)
# print(kume1)

# kume kesişimleri - intersection()
# kume1 = {1,2,3,4,5,6}
# kume2 = {4,5,6,7,8,9,10}
# kume1.intersection(kume2)
# print(kume1)
# print(kume2)
# print(kume1.intersection(kume2))

#intersection_update()
# kume1 = {1,2,3,4,5,6}
# kume2 = {4,5,6,7,8,9,10}
# kume1.intersection_update(kume2)
# print(kume1)

#ayrık küme mi -isdisjoint()
# kume1 = {1,2,3,4,5}
# kume2 = {6,7,8,9,10}
# kume3 = {1,11,111,1111}
# print(kume1.isdisjoint(kume3))

# alt kümesi mi - issusubset()
# kume1 = {1,2,3,4,5}
# kume2 = {1,2,3,4,5,6,7,8}
# kume3 = {7,77,777}
# print(kume1.issubset(kume3))

# birleşim kümesi - union
# kume1 = {1,2,3,4,5}
# kume2 = {6,7,8,9,10}
# print(kume1.union(kume2))

# update()
kume1 = {1,2,3,4,5}
kume2 = {6,7,8,9,10}
kume1.update(kume2)
print(kume1)