#Girilen sayı hem 3 hem de 5’e tam bölünüyorsa “15’e tam bölünür.”; bölünmüyorsa “15’e tam bölünmez.” çıktısını veren python kodunu yazalım.
sayi = int(input("Bir sayı girin :"))
 
if sayi % 5 ==0 and sayi % 3 == 0 :
  print("15'e tam bölünür")
else:
  print("15'e tam bölünmez.")




