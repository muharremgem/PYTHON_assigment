#Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdıran python kodlarını yazalım. 0 -24 => 0 25-44 => 1
#45-54 => 2
#55-69 => 3
#70-84 => 4
#85-100 => 

x = int(input("Birinci yazılı notu: "))
y = int(input("ikinci yazılı notu : "))
z = int(input("sözlü notu : "))
if (x+y+z)/3 >= 85 :
  print(5)
elif (z+y+z)/3 >= 70:
  print(4)
elif (x+y+z)/3 >= 55:
  print(3)
else:
  print(2);
