"""
# zar atıldıgında gelme olaslıkları for dongusu ile
import random 

zarlar = { 1: 0,2: 0,3: 0,4: 0,5: 0,6: 0}   # sayıları 0 olarak atadık

for i in range(1000000):               # 100000 kere atıldıgında
    zar = random.randint(1 , 6)       # 1 ıle 6 arasında 6 dahıl  random sayı atar 
    zarlar[zar] += 1                  # zarlar atıldıktan sonra 1 arttırır 



for zar in zarlar:                   
    print(f"{zar} gelme olsılıgı :  {zarlar[zar] / 1000000} : ")   # zarların gelme ıhtımalını hesaplar
  

"""

# # zar atıldıgında gelme olaslıkları  while dongusu ile

import random      # random fonksıyonu tanımlandı

alti_alti = 0          #  kac kere 6,6 geldı , hıc 6,6  gelmedı
deneme_sayisi = 0      # kac kere zar attı
while True:            #  kosul dogru oldukca donguye devam 
    deneme_sayisi += 1  
    zar1  = random.randint(1,6)     # 1 ıle 6 arasında zar atıldı
    zar2  = random.randint(1,6)
    if zar1 == 6 and zar2 == 6:    # 1.ve 2. zarın altıya esıt oldugu sorgulandı
        alti_alti  +=  1            # 6-6 sayısını 1 arttır
    if alti_alti == 100:          # 6-6 100 tane oldu mu dıye sorgula
        print(f"100 kere 6-6 gelesi için zarlar {deneme_sayisi} kadar atıldı. ")
        break   # f fonksıyonuyla yazdır ve donguyu kır

    













