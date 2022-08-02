#  Girilen 2 sayı arasındaki sayıların toplamını bulan kodları for döngüsü kullanarak yazalım
sayi1=int(input("Başlangıç Değerini Girin : "))
sayi2=int(input("Bitiş Değerini Girin : "))
 
toplam=0
for i in range(sayi1,sayi2+1):
  toplam+=i
  
print("Sayıların Toplamı: {}".format(toplam))