# input sadece string  ıfade alır int ıcıne yazarak ınt degısken alırız
print(""" hesap makinesi """)
sayi1=float(input("birini sayıyı girininiz :"))   # kullanıcıdan 1. degişkeni aldırdı
sayi2=float(input("ikinci sayıyı giriniz :"))     # kullanıcıdan 2. degişkeni aldırdı

print("""
toplam = {}            # toplama işlemini yaptırdı 
fark = {}              # cıkarma  işlemini yaptırdı
bolum ={}              # bolme  işlemini yaptırdı
carpım ={}
""".format(sayi1+sayi2,sayi1-sayi2,sayi1/sayi2,sayi1*sayi2))