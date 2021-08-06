print("Programıma Hoşgeldiniz...","Kitaptakip v1.0")
#Program kitap ekleme, sayfa güncelleme işlemlerini yapıyor.
#Progarama kitap ekleme bölümü olamlaı
#Eklenen veri üzerinde sonradan değişim yapabilmeli
#Kitap bitti uyarısı 
#Veri girişi yapılmadığı günler için uyarı gibi bir yazı
#İLerisi için hedef konulabilir

while True:
    seçenekler=input("""Kitap eklemek için:"e"
Okunmuş sayfaları güncellemek için:"g"
Programdan çıkmak için:"ç"
tuşlarına basınız...""")
 #Kitap ekleme bölümü buradan   
    
    if seçenekler == "e":
        kitap_adı=input("Kitabın Adını Giriniz:")
        kitap_yzr=input("Kitabın Yazarını Giriniz:")
        kitap_sayfa=int(input("Kitbaın toplam sayfasını giriniz:"))
        eklenen = "\n{}     {}\t: {}".format(kitap_adı,kitap_yzr,kitap_sayfa)
    
        with open("kitaptakip.txt","a+") as f:
            f.write(eklenen)
        
        #eklenen=print("{}/{} sayfa:{}".format(kitap_adı,kitap_yzr,kitap_sayfa),file=f,flush=True)
        print("{} adlı kitabınız {} sayfa olarak kaydedildi".format(kitap_adı,kitap_sayfa))
        continue
        
    elif seçenekler == "g":
        #kitap_değişim=input("Okuduğunuz sayfa sayısını güncellemek istediğiniz kitabın adını yazınız:")
        #sayfa_değişim=input("Şu anda bulunduğunuz sayfa sayısını yazınız:")
        #print("{} adlı kitapta {} sayfadasınız.".format(kitap_değişim,sayfa_değişim))
        #print("{} adlı kitapta {} sayfadasınız.".format(kitap_değişim,sayfa_değişim),file=f,flush=True)
        with open("kitaptakip.txt","r+") as g:
            veri=g.readline
            print(veri)
            
    elif seçenekler == "ç":
        print("Program Kapatılıyor. İyi okumalar...")
        break       
