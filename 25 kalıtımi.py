"""

class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas

        def bilgileriyazdır(self):
            print("""
                  
{}  {} bildileri şunlardır
yas:{}                  
cinsiyet: {}       
maas: {}
""".format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas))
         def __str__(self):
               return """  {}  {} bildileri şunlardır
yas:{}                  
cinsiyet: {}       
maas: {}
""".format(self.ad,self.soyad,self.yas,self.cinsiyet,self.maas)   
Personel  = personel("asaf","pınar","19","erkek","200000")
print(personel)

"""


