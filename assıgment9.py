"""Task:
Find out if a given number is an "Armstrong Number".
An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 33 + 73 + 13;
9474 = 94 + 44 + 74 + 44;
93084 = 95 + 35 + 05 + 85 + 45.
Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user."""
try:
    num = int(input("Enter a number:\n"))
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num < 0:
        print("Please enter positive value")
    elif num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
except:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")