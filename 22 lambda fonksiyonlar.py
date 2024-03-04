""""
a = 10 

def islem(b,c) :  # işlemi taanımladı 
    print(a)

    return b*c*a    
print(islem(7,6))
      
"""      
      
"""
c = 10

def carp(a,b):

	c = 5
	print("fonksiyonun içinde c : ",c)
	print(a*b)

carp(2,9)
print("fonksiyonun dışında c : ",c)
 çıktı 
>>> fonksiyonun içinde c : 5
>>>  18
>>> fonksiyonun dışında c : 10
"""


   #   fonksiyon = lambda degişkenler:dönecek deger  
   # def fonksiyon(degişkenler)
   #  return donecekdeğer

toplam =  lambda *sayilar : sum(sayilar)
print(toplam(480,455,298,190,789))