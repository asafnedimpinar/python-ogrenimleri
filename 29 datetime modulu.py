
from datetime import date   # dati datetime sınıfından tanımladık

bugun = date.today()  # bugunu tarıh olarak atadık
print(bugun)        # bugunun tarıhını yazdı
print(type(bugun))   # bugunun veri tıpını yazdırdı
print(bugun.month)   # bugun tarıhının ayını yazdırdı
print(bugun.year)    # bugun tarıhının yılını yazdırdı
print(bugun.weekday)  # bugunun haftanın kacıncı gunu oldugunu yazdırır


gecmis_tarih = date(2015,9,22)   #gecmıs tarıhı ekrana yazdırdık
print(gecmis_tarih)


















