Sifre = 12345
K_adı = "asaf"
while True:
    Kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    if Kullanici_adi == "0":
        break
    elif Kullanici_adi != K_adı:
        print("Kullanıcı adı hatalı, lütfen tekrar deneyin.")
    elif Kullanici_adi == K_adı:
        sifre1 = input("Şifrenizi giriniz: ")
        if Sifre != sifre1:
            print("Şifre hatalı.")
        elif Sifre == sifre1:
            print("Giriş yapılıyor.")
        else:
            print("Lütfen şifreyi giriniz.")
    else:
        print("Lütfen kullanıcı adınızı giriniz.")

