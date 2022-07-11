# Belirli bir sayı grubu içindeki sayılardan üçe tam bölünenleri listeyen kodları for döngüsü ile yazalım.
numbers = [3, 7, 11, 12, 14, 21, 65, 66, 90]
new_list = []
for i in numbers:
  if i%3 == 0 :
    new_list.append(i)
print(new_list)