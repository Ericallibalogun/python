number = int(input('Enter a five digit number: '))
first = int(number / 10000)
second = int(number / 1000) % 10
third = int(number / 100) % 10
fourth = int(number / 10) % 10
fifth = int(number % 10)

print(first," ",second," ",third," ",fourth," ",fifth)