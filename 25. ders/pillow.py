from PIL import Image, ImageFilter

image = Image.open("kus.jpeg")

# image.save("kus2.jpeg")
# image.rotate(180).save("kus3.jpeg")
# image.rotate(90).save("kus4.jpeg")
# image.convert(mode="L").save("kus5.jpeg")

# degistir = [960,600]
# image.thumbnail(degistir)
# image.save("kus6.jpeg")

# image.filter(ImageFilter.GaussianBlur(12)).save("kus7.jpeg")

# kirpilacak_alan = (340,0,950,600)
# image2 = Image.open("ataturk.jpg")
# image2.crop(kirpilacak_alan).save("ataturk2.jpg")

image.show()