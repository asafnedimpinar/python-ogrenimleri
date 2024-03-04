# and baglacı dogru dogru olursa true degirisi false
# or baglacı yanlıs yanlıs olursa false gerisi true olur

kullanıcıbilgileri= ["asdas98","1234567k"]
kadi = input("kullanıcı adını giriniz :")
sifre= input("şifreyi giriniz :")
a = kullanıcıbilgileri[0] == kadi and kullanıcıbilgileri[1] == sifre
print(a)