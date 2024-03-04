

yazı= "Benım adım Hasan Cabbar . Pariste yasıyorum"

#sonuc =yazı.upper()  # upper metodu tum harflerı buyuge donusturur 
#sonuc=yazı.lower()   # lower metodu tum harflerı kucuk yapar
#sonuc=yazı.title()    # title metodu bas harflerın buyuk yapar
#sonuc=yazı.capitalize()  # sadece ılk bastakı harfı buyuk yapar
#sonuc=yazı.isupper()   # hepsı buyukmu dıye sorgular
#sonuc=yazı.strip()     # bastakı ve sondakı boslukları kaldırır
#sonuc=yazı.split()      # dızı olurturur "" icinde kuralını verırsen o kurala gore ayırır
#sonuc="-".join(yazı)   # herseyı ayırır aralarına - koyar
#sonuc=yazı.index("y")   # "y "ın nerede oldugunu bulur
#sonuc=yazı.startswith("y")   # y harfının var olup olmadıgına bakar
#sonuc=yazı.endswith("m")      # sonu m ıle bıtıyormu dıye bakar 
# sonuc=yazı.replace("adım",("ısmım"))  # adım kelımesını ısmım kelımesıyle yer degıstırır
sonuc=yazı.replace("ı","i").replace("s","ş") # seklınde de kullanılanılır
 
 
print(sonuc)








