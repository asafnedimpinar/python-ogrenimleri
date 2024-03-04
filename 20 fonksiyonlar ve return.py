def tekçift(sayi):
    if sayi % 2 == 1 :   # sayı tekse direkt döngüden cıkartır 
        return sayi
    
    toplam = 0 
    for i in range(1,sayi+1): # sayı çiftse 1 den o na kadar olan sayıları toplar 
        toplam += i

    return toplam
print(tekçift(24))
   