#Kullanıcıdan kullanıcıad� ve �ifre girilmesi isteniyor. Kullan�c� ad� �T�rkiye�; �ifre 1923 ise �Giri� ba�ar�l��; de�ilse �Kullan�c� ad� ya da �ifre yanl��� ��kt�lar� veren kodu yazal�m.
kullanici_adi =input("Kullanıcı adı girin :")
sifre = input("Kullanıcı şifresi girin :")
 
if kullanici_adi=="Türkiye" and sifre=="1923":
  print("Giriş Başarılı")
else:
  print("Kullanıcı adı yada şifre hatalı")