def kucuk(a, b):  # İki parametre alarak küçük olanı döndüren bir fonksiyon tanımlanıyor.
    if a < b:     # Eğer 'a', 'b'den küçükse,
        return a  # 'a' değeri döndürülüyor.
    elif b < a:   # Eğer 'b', 'a'dan küçükse,
        return b  # 'b' değeri döndürülüyor.

    return a      # 'a' ile 'b' eşitse, herhangi biri döndürülebilir.

print(kucuk(20, 70))  # Fonksiyon çağrılıyor ve 20 ve 70 parametreleriyle çağrıldığında, küçük olan 20 olduğu için ekrana 20 yazdırılıyor.

c = 10   # Global bir değişken tanımlanıyor.

def carp(a, b):  # İki parametre alarak çarpma işlemi yapan bir fonksiyon tanımlanıyor.
    global c     # Global 'c' değişkeninin kullanılacağı belirtiliyor.
    c = 5        # Fonksiyonun içinde 'c' değişkeninin değeri 5 olarak güncelleniyor.

    print("fonksiyonun içinde c : ", c)  # 'c' değişkeninin fonksiyonun içindeki değeri ekrana yazdırılıyor.
    print(a * b)                         # İki parametrenin çarpımı ekrana yazdırılıyor.

carp(2, 9)       # Fonksiyon çağrılıyor.
print("fonksiyonun dışında c : ", c)  # Fonksiyonun dışında 'c' değişkeninin değeri ekrana yazdırılıyor.





