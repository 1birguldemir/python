#key-value
# sozluk1 = {"freedom":"özgürklük","hourse":"at","house":"ev"}
# print(sozluk1)

# sozluk1 = {}
# print(sozluk1) 

# sozluk1 = dict()
# print(sozluk1)

# sozluk1 = {"freedom":"özgürklük","hourse":"at","house":"ev"}
# print(sozluk1["freedom"])

# sozluk1 = {"bir": [1,2,3,4],"iki":[[1,2],[3,4],[5,6]],"üç":15}
# sozluk1["iki"][2][1]+=10
# print(sozluk1["iki"][2][1])


# sozluk1 = {"freedom":"özgürklük","hourse":"at","house":"ev"}
# sozluk1["man"]="adam"
# print(sozluk1)

# sozluk = {"sayilar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
# print(sozluk["sayilar"]["üç"])
# print(sozluk["meyveler"]["kiraz"])

sozluk1 = {"freedom":"özgürklük","hourse":"at","house":"ev"}
print(list(sozluk1.values()))
print(list(sozluk1.keys()))
print(list(sozluk1.items()))

