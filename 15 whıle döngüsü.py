# whıle dongusu kosul saglangı surece domeye devam eder
import random  #random sayı atar
yazigelen = 0
turagelen = 0

parayuzeyi = ["tura","yazi"]

atılacakpara = int(input("kac kere parayı atmak istiyorsunuz :"))

while atılacakpara > 0:
    paraustu = random.choice(parayuzeyi)  # random seçim yapar 
    if paraustu == "tura":
        turagelen+=1
        print("tura geldi")
    else:
        yazigelen+=1
        print("yazı geldi")

    atılacakpara-=1
    print("tura sayısı : {}\n yazı sayısı : {}".format(yazigelen,turagelen))

