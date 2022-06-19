#Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.
#Task-2:Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.
###############################
celsius = float(input('Ceslius derece girin:'))    # fahrenhayt hesapla
fahrenheit = (celsius * 1.8) + 32
print('%0.1f Celsius derece ,%0.1f Fahrenheit derecesine eşittir' %(celsius,fahrenheit))
#####

kilometre = float(input("kilometreyi giriniz: ")) # mil hesapla 
oran = 0.621371
mil = kilometre * oran

print('%0.2f kilometre %0.2f mil yapar' % (kilometre,mil))






