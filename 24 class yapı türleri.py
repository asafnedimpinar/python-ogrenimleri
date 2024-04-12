
class Araba():
    """
    Araba sınıfı, araba nesnelerinin özelliklerini ve davranışlarını tanımlar.
    """

    def __init__(self, marka, model, fiyat, renk):
        """
        Araba sınıfının başlatıcı yöntemi. Yeni bir araba nesnesi oluşturur.

        Parametreler:
            marka (str): Arabanın markası.
            model (str): Arabanın modeli.
            fiyat (int): Arabanın fiyatı.
            renk (str): Arabanın rengi.
        """
        self.gelenmarka = marka  # Arabanın markası
        self.gelenmodel = model  # Arabanın modeli
        self.gelenfiyat = fiyat  # Arabanın fiyatı
        self.gelenrenk = renk    # Arabanın rengi

    def bilgileriyazdır(self):
        """
        Arabanın bilgilerini ekrana yazdıran metot.
        """
        print(self.gelenmarka, self.gelenmodel, self.gelenfiyat, self.gelenrenk)


# Araba nesneleri oluşturma
araba1 = Araba("bmw", "i30", 30_000, "mavi")
araba2 = Araba("mercedes", "e5", 50_000, "siyah")

# Araba bilgilerini yazdırma
araba1.bilgileriyazdır()
araba2.bilgileriyazdır()
Bu şekilde, her bir metodu ve parametreyi neyin temsil ettiğini açıklayan açıklamalar eklenmiştir.



