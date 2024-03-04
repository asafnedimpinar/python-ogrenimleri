"""
age = "19"
name = "ahmet"
surname = "bozkıran"

text = " benim adım " + name + " ve soyadım " + surname + " yasım ıse " + age  + "."  # bilestirme metodu
 
print(text)
print(text[0:5]) # 0 dan başla 5 kadar git
print(text[6:19]) # 6dan basşla 19 a git
print(text[:20])  #bastan baslar sonda durur
print(text[10:]) # 10 dan baslar bitince  durur
print(text[-20:-1]) # 20. indeksten basladı sonuncuya kadar
print(text[0:30:2]) # 0 dan basla 30 a kadar 2 2 atlayarak git
print(text[::2])  # 2 2 atlayarak tamamını yazdırır
print(text[::-1]) #tersten yazdırır


password =  "abc12345"
print(password[0])  # a yı al

print(password[-2]) # 4 sondan iknciyi al
"""

age = "19"
name = "ahmet"
surname = "bozkıran"

print("adım {} {}".format(name,surname)) # name ve surnamı alır ({}".format())
print("adım {1} {0}".format(name,surname)) # istedigi yeri yazar
print("adım {s} {n}".format(n=name,s=surname))  # degisken tanımlayıp yerlerini istedigimiz gıbı degıstırırız
print("adım {} {} ve yasım {} dır".format(name,surname,age) )  # bu sekılde de saglanır 
print("adım {0} {1} ve yasım {2} dır {0}".format(name,surname,age) )   # adı 2 kere kullandı 

number= 5/3
print("the result is{n:1.6}".format(n=number))  # n den basla 1 tam ve ondalıklı kısımda 6 ya kadar olanları al cıktı=1.66667

print(f"benım adım {name} {surname} ve {age} yasındayım ") # en kolay bırlestırme yontemi f yaz tırnak ac {} nun ıcıne ne cagıracaksan yaz
