""" # dongü saglanırsa 1. yazılır eger koşul sağlanmazsa dongü kırılır ve ıkınci print yazdırılır

while True:
    sayi = int(input("bir sayı giriniz : (sayı tek olursa döngü biter)"))

    if sayi % 2 == 1 :
        break
    print("döngünün sonu")

print("döngünün dışı")
"""

while True :
    sayi = int(input("bir sayı giriniz : (eger tek sayı girerseniz yazılmıcaktır)"))
    if sayi % 2 == 1 :
        continue
    print(sayi)