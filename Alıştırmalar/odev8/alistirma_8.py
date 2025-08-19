# 1. problem
# liste = ["345","sadas","324a","14","kemal"]
# for i in liste:
#     try:
#         sayi = int(i)
#         print(sayi)
#     except ValueError:
#         print("Value error hatası")


# 2.problem

def cift_sayilar(i):
    if i % 2 == 0:
        return i
    else:
        raise ValueError("Value error hatası")
    
liste = [1,2,3,4,5,6,7,8,9,10]   
for i in liste:
    try:
        print(cift_sayilar(i))
    except ValueError as e:
        print(e)
