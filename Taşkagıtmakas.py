import random
secenek=["t","k","m"]
t=secenek[0]
k=secenek[1]
m=secenek[2]
print("Taş,Kağıt, Makas oyununa hoş geldinizn Oyunu bitirmek için q tuşuna basın")
bil_puan = 0
puan = 0
while True:
    secim = input("Taş mı kağıt mı makas mı? ")
    bil_secim = random.choice(secenek)
    if secim==t:
        if bil_secim==t:
            print("Bilgisayarın seçimi: TAŞ \n Sonuç : BERABERE")
        elif bil_secim==k:
            bil_puan += 1
            print("Bilgisayarın seçimi: KAĞIT \n Sonuç : KAYBETTİN")
        else:
            puan += 1
            print("Bilgisayarın seçimi: MAKAS \n Sonuç : KAZANDIN !!")
    if secim==k:
        if bil_secim==t:
            puan += 1
            print("Bilgisayarın seçimi: TAŞ \n Sonuç : KAZANDIN !!")
        elif bil_secim==k:
            print("Bilgisayarın seçimi: KAĞIT \n Sonuç : BERABERE")
        else:
            bil_puan += 1
            print("Bilgisayarın seçimi: MAKAS \n Sonuç : KAYBETTİN")
    if secim==m:
        if bil_secim==t:
            bil_puan += 1
            print("Bilgisayarın seçimi: TAŞ \n Sonuç : KAYBETTİN")
        elif bil_secim==k:
            puan += 1
            print("Bilgisayarın seçimi: KAĞIT \n Sonuç : KAZANDIN !!")
        else:
            print("Bilgisayarın seçimi: MAKAS \n Sonuç : BERABERE")
    if secim=='q':
        if bil_puan > puan:
            print(f"OYUN BİTTİ {bil_puan}-{puan} kaybettin")
        elif puan > bil_puan:
            print(f"ÇOK İYİ OYNADIN , {puan}-{bil_puan} KAZANDIN !!")
        else:
            print(f"OYUN {puan}-{bil_puan} BERABERE BİTTİ")
        break