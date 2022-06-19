#Task : Find out the most frequent number and its frequency.Write a program that;Finds out the most frequent number in the given list.Calculates its frequency.Prints out the result such as :
#
numbers = [1,3,7,4,3,0,3,6,3]
max_count = 0
num = numbers[0]
for i in numbers :
  a = numbers.count(i)
if a >= max_count:
  max_count = a
  num = i 
print(f"The most frequent numbers is {num} and it was {max_count} times repeated")

