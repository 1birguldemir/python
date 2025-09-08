import sys 

# a = input("a: ")
# b = input("b: ")

# sys.exit()

# c = input("c: ")

# stdin - stdout - stderr
import sys
sys.stderr.write("Hata mesaajı\n")
sys.stderr.flush()
sys.stdout.write("Standart çıktı mesajı \n")