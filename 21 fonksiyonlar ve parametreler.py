"""
def kucuk(a,b):        # kucuk olan sayıyı alır
    if a<b :
       return a
    elif b<a :
       return b
    
    return a 
print(kucuk(20,70))
"""



c = 10

def carp(a,b):

	global c
	c = 5

	print("fonksiyonun içinde c : ",c)
	print(a*b)

carp(2,9)
print("fonksiyonun dışında c : ",c)










