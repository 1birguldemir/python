def fibonacci():
    a = 1 
    b = 1
    yield a
    yield b
    while True:
        a ,b = b, a+b
        yield b

# generator = fibonacci()
# iterator = iter(generator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for sayi in fibonacci():
    if sayi > 15000:
        break
    print(sayi)