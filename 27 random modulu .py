 
"""

import random 

for i  in range (10):                # 10 tane sayı  al demek
    print(random.random())           # random. random 0 la 1 arasında random sayı uretır
"""




"""
import random 

for i in range(10):                 # 10 tane sayı uretır
    print(random.uniform(10,30))    #  unıfor bızım belırledıgımız sayılar arasında sayı uretır
                                    # unıformda sınırlar dahıl degıl

 """


"""

import random

for i in  range(7):               # 7 tane sayı al i nin ıcınden
    print(random.randint(1,5))    # rand ınt tam sayı uretır 
                                  # sınırlar dahildir

                                  
"""




"""

import random

for i in range(8):                      # 8 tane sayı al i nin icinden 
    print(random.randrange(1,19,4))     # 1 den 19 a kadar aralarında 4 tane bosluk alan sayıları al   
                                        # ust sınır dahıl degıl


"""



import random 

liste = ["siyah","beyaz","yeşil","dri","kırmızı"]
random.shuffle(liste)              # liste yazılırken sırasını random degıstırır

#  print(randm.sample(liste,3))    # listeden 3 tane rastgele eleman secer

print(liste)












