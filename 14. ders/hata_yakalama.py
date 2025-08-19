# try, except, finally
# try:
#     pass
#     #bizim kod bloğumuz
# except:
#     print("Kodlarınızda hata oluştu.")


# try:
#     a = int("123slfkdk")
# except:
#     print("Hata oluştu.")

# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")
# print("Bloklar sona erdi.")


# try:
#     # a = int("123fghnfhjmnhfg")
#     print(2/0)
#     print("program burada")
# except ValueError:
#     print("Value error hatasını yakaladık")
# except ZeroDivisionError:
#     print("Sıfıra bölme hatasını yakaladık.")
# finally:
#     print("Her durumda çalışıyorum.")
# print("bloklar sona erdi.")


def ters_cevir(yazi):
    if type(yazi) != str:
        raise ValueError("Lütfen string bir değer giriniz.") 
    else:
        return yazi[::-1]
    
# handle etmek - kontrol altına almak
try:
    print(ters_cevir(88888))
except (TypeError,ValueError) as e:
    print(e)
except ZeroDivisionError:
    print("sıfıra bölme...")
except :
    print("genel except bloğu...")