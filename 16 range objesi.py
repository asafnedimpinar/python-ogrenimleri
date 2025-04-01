"""
for i in range(20,1000,5): # 20 baslangıc degeri ,1000 bitis degeri, 5 atlıcagı deger ( baslangıc-bıtıs-adım)
    print(i)
for a in range(200): # 0 dan 200 e kadar 1 1 yazdırır
    print(a)
for z in range(40,900): # 40 tan 900 e  kadar olan sayıları 1 1 yazdırır
    print(z)
 """

def asal_mı(sayi):    
 for i in range(2,sayi):
   if sayi %i == 0 :
     return False 
   return True

sayi = int(input("sayi giriniz :"))
asal_sayilar = []

for i in range(2,sayi+1):
  if asal_mı(i):
    asal_sayilar.append(i)

print(asal_sayilar)
