#Using the all following items once each, set a correct boolean expression that returns write me. Use the print() function to display the result.
# (0,  and,  not,   "write me")
print(not 0 and "write me")
################################
#Task:Find out if a given year is a "leap" year.
#In the Gregorian calendar, three criteria must be taken into account to identify leap years:
#The year must be evenly divisible by 4;
#If the year can also be evenly divided by 100, it is not a leap year; unless...
#The year is also evenly divisible by 400. Then it is a leap year.
#According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
#Write a Python program that;
#Takes a 4-digit year from the user,
#Prints True if the given year by the user is a leap year, prints False otherwise.
#Note that; this question is famous on the web, so that do it yourself to get more benefits from it.


yil = int(input("enter a 4-digit year: ")) 

x = yil % 4 == 0 

y = yil % 100 != 0 

z = yil % 400 == 0 

leap = x and z or y

print(leap)

