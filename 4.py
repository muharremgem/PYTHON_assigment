#Girilen 3 sayıyı büyüklük olarak karşılaştırmasını yapan Python kodlarını yazalım.

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))
sayi3 = int(input("3. Sayı: "))
 
if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   buyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   buyuk = sayi2
else:
   buyuk = sayi3
 
print(sayi1,",",sayi2,"ve",sayi3,"içinde büyük olan sayı",buyuk)


