import math

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

sum = first + second + third
print('the sum :',sum)
average = sum / 3
print('the average :',(round(average,2)))
#print(f"The average is :{average:.2f}")
product = first * second * third
print('the product :',product)

smallest = first
if smallest < second:
    smallest = second
if smallest < third:
    smallest = third
print('the smallest :',smallest)

largest = second
if largest > first:
    largest = first
if largest > third:
    largest = third
print('the largest :',largest)