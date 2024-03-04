"""
import time

time = time.time()    # zaman baslangıcı kabul edılen tarıhten bu yana kac sn gectıgını gosterır
print(time)

"""


"""
import time
baslangıc = time.time()     # baslangıc zamanını tanımladık
liste  = []
for i in range(10000000):   # yapılacak ıslem
    liste.append(i)
bitis = time.time()        # bıtıs zamanı
print(baslangıc-bitis)      # baslangıc ve bıtıs arasında gecen sureyı yazdırır 


"""


"""
import time

time = time.ctime(1000000)   #baslangıctan ıtıbaren gecen sanıyenın tarıhını verır
print(time)

"""


"""
import time

time = time.localtime(100000000)   #  baslangıctan ıtıbaren gecen zamanı tarıhı bileşenlerine ayırır
print(time)
"""

"""

import time 

time2 = time.localtime()   #  baslangıctan ıtıbaren gecen zamanı tarıhı bileşenlerine ayırır
time =  time.asctime(time2)   # bilesenlerıne ayrılmıs tarıhı duzeltıp yazdırır 
print(time)          # icindekı bılesık tıple veya struck olmak zorunda or tıme 2 

"""


import time


time = time.strftime("%D:%Y")   # zamanı sıtedıgımız sekilde yazdırabılmemızı saglar 
print(time)






