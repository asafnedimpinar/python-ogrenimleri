# hesapmakinesi.py

import hesapmakinesi



def topla(x,y):
     return x + y
 
def cikar(x, y):
     return x - y
 
def carp(x, y):     #moduller işlemleri ayırarak kısaltmaya yarar 
    return x * y
 
def bol(x, y):
    return x / y





import hesapmakinesi as hm         # hesap makınesını hm adında modul yaptık yer kaplamasın dıye

print(hm.carp(5, 6))
print(hm.topla(5, 6))
print(hm.cikar(5, 6))
print(hm.bol(5, 6))
  #>>> 30  >>> 11
"""


demet_1 = ("Python","Ruby","C++")

sözlük_1 = {"Python": ".py", "Ruby": ".rb", "C++": ".cpp"}

print(type(demet_1))
print(type(sözlük_1))
"""