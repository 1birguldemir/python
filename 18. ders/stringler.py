# upper() - lower()
# yazi = "alİ-ata-Bak."
# print(yazi.lower())

# replace()
# print(yazi.replace("a","e"))

# startswith() - endswith()
# print(yazi.startswith("alİ"))
# print(yazi.endswith("Bak."))

# split()
# print(yazi.split("-"))

# strip() - lstrip()- rstrip()
# yazi = "XXXXXXXXXXXXXXXXXXXbirgül demirXXXXXXXXXXXXXXXXXXX"
# print(yazi.strip("X"))
# print(yazi.lstrip("X"))
# print(yazi .rstrip("X"))

# join()
# liste = ["21","02","2025"]
# print("/".join(liste))

# liste = ["T","B","M","M"]
# print(".".join(liste))

# count()
yazi = "türkiye büyük millet meclisinde türkiye ile ilgili konular türkiyede görev yapan millet vekillerince görüşüldü."
# print(yazi.count("türkiye",20))

# find() - rfind()
# print(yazi.find("millet",20))
print(yazi.rfind("millet"))