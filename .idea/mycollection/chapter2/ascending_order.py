num1 = float(input("Enter first floating number: "))
num2 = float(input("Enter second floating number: "))
num3 = float(input("Enter third floating number: "))

lowest = num1
if lowest < num2:
    lowest = num2
if lowest < num3:
    lowest = num3

highest = num2
if highest > num1:
    highest = num1
if highest > num3:
    highest = num3

middle = num3
if middle > lowest or middle < highest:
    middle = middle

print(lowest,middle,highest)