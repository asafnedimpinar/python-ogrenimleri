sayi =int(input("bir sayı giriniz: "))

if sayi % 2 == 1 :
   print("girdiginiz {} sayısı tektir".format(sayi))   # şartı saglarsa döngüden çıkar sağlamazsa else girer
else :
   print("girdiğiniz {} sayısı çifttir".format(sayi))