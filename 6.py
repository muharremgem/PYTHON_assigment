#1-100 arası Çift Sayıları Listeleyen Python kodlarını yazalım.
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