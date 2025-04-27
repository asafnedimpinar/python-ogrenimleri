
print(""" Hesap Makinesi """)

# Kullanıcıdan ilk sayıyı alarak float tipine dönüştürme
sayi1 = float(input("Birinci sayıyı giriniz:"))

# Kullanıcıdan ikinci sayıyı alarak float tipine dönüştürme
sayi2 = float(input("İkinci sayıyı giriniz:"))

# Toplam, fark, bölüm ve çarpım işlemlerini ekrana yazdırma
print("""
Toplam = {}            # İki sayının toplamını yazdırma
Fark = {}              # İki sayının farkını yazdırma
Bölüm = {}             # İki sayının bölümünü yazdırma
Çarpım = {}            # İki sayının çarpımını yazdırma
""".format(sayi1 + sayi2, sayi1 - sayi2, sayi1 / sayi2, sayi1 * sayi2))
