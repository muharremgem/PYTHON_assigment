
n = int(input("How many numbers will you enter?:"))
sayı = []

for i in range(n) :
    n1 = int(input("please enter the number"))
    sayı.append(n1)
en_buyuk = sayı[0]
for i in sayı:
  if en_buyuk < i :
    en_buyuk = i

print("liste içindeki en buyuk sayı :", en_buyuk)
