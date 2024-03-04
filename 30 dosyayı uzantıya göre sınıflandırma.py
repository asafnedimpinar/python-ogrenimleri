import os



def duzenle(): 
    klasor = input("Düzenlenecek Klasör : ")
    dosyalar = []  # dosyalar depolanacak 
    uzantilar =[]   # uzantılar depolanacak 
    def list_dir() :
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)):   # dosya klasor mu sorguladı
                continue
            if dosya.startswith("."):   #dosyanız bir gizli dosya mı
                continue
            else:
                 dosyalar.append(dosya)
    list_dir()                       # uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar:    # uzantı daha önce eklendi mi
           continue 
        else:
           uzantilar.append(uzanti)
    for uzanti in uzantilar:    # klasörler oluşturuluyor
        if os.path.isdir(os.path.join(uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor,uzanti)) # klasör uzantı
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya),os.path.jon(klasor,uzanti,dosya))
if __name__== "  main  ":    # bir fonksiyon import ettigimizde bütün  fonlsiyonu degil sadece istedigimiz kısmı calıstırmak icin kullanırız
    duzenle()

    
  
