# and baglacı dogru dogru olursa true degirisi false
# or baglacı yanlıs yanlıs olursa false gerisi true olur
# Kullanıcı bilgilerini içeren liste
kullanıcıbilgileri = ["asdas98", "1234567k"]

# Kullanıcıdan kullanıcı adını girmesini isteme
kadi = input("Kullanıcı adını giriniz: ")

# Kullanıcıdan şifreyi girmesini isteme
sifre = input("Şifreyi giriniz: ")

# Kullanıcının girdiği kullanıcı adı ve şifrenin doğruluğunu kontrol etme
# Eğer kullanıcı adı ve şifre listedeki bilgilerle uyuşuyorsa 'True', aksi takdirde 'False' değeri atanır
a = kullanıcıbilgileri[0] == kadi and kullanıcıbilgileri[1] == sifre

# Sonucu ekrana yazdırma
print(a)
