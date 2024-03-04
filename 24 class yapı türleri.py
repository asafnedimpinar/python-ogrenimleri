"""

class araba():
    def __init__(self,marka,model,fiyat,renk) :
        self.gelenmarka : marka
        self.gelenmodel : model
        self.gelenfiyat : fiyat
        self.gelenrenk : renk


    def bilgileriyazdır(self):
        print(self.gelenmarka,self.gelenmodel,self.gelenfiyat,self.gelenrenk)

araba1 = araba("bmw","i30",30_000,"mavi")
araba2 = araba("mercedes","e5",50_000,"siyah")


araba1.bilgileriyazdır()
araba2.bilgileriyazdır()
"""


class Araba():
    renk = "kirmizi"
    model= "Clio"
    fiyat = 50_000
    marka ="renault"
    
    
    
    def Yaz(self):
        print(self.renk,self.model,self.fiyat,self.marka)