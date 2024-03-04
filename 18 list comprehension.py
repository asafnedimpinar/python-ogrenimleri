""" 
sayilar =  [ x  for x in range(1,100_001) if x % 2 == 0 and x % 3 == 0 ]

print(sayilar)
"""

kişiler = ["melda","mert","merve","ece","havva","asaf","nedim"]

m_ile_başlayan = [kişi for kişi in kişiler if "m" in kişi ] # uzun bir dongü olusturmak yerine kısa bir sekilde kurduk

print(m_ile_başlayan)
