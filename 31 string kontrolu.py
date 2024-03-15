# Doğru kullanıcı adı ve şifre tanımlanıyor
Sifre = 12345
K_adı = "asaf"

# Sonsuz döngü başlatılıyor
while True:
    # Kullanıcıdan kullanıcı adı isteniyor
    Kullanici_adi = input("Kullanıcı adınızı giriniz: ")

    # Eğer kullanıcı "0" girerse döngüden çıkılıyor
    if Kullanici_adi == "0":
        break
    # Eğer girilen kullanıcı adı tanımlanan kullanıcı adıyla uyuşmuyorsa hata mesajı veriliyor
    elif Kullanici_adi != K_adı:
        print("Kullanıcı adı hatalı, lütfen tekrar deneyin.")
    # Eğer girilen kullanıcı adı tanımlanan kullanıcı adıyla uyuşuyorsa şifre isteniyor
    elif Kullanici_adi == K_adı:
        sifre1 = input("Şifrenizi giriniz: ")
        # Eğer girilen şifre tanımlanan şifreyle uyuşmuyorsa hata mesajı veriliyor
        if Sifre != sifre1:
            print("Şifre hatalı.")
        # Eğer girilen şifre tanımlanan şifreyle uyuşuyorsa giriş yapıldığına dair mesaj veriliyor
        elif Sifre == sifre1:
            print("Giriş yapılıyor.")
        # Girilen şifre boşsa veya yanlış bir değerse hata mesajı veriliyor
        else:
            print("Lütfen şifreyi giriniz.")
    # Kullanıcı adı boşsa veya yanlış bir değerse hata mesajı veriliyor
    else:
        print("Lütfen kullanıcı adınızı giriniz.")

