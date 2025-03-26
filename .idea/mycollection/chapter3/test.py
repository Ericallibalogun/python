#grade = str(input("Enter the user's grade : "))

#result = 'Passed' if grade >= 60 else 'Failed'
#print (result)

#for character in 'Programming':
    #print(character, end=',')

#total = 0
#for number in [2, -3,0,17,9]:
    #total += number
#print("\n",total)

#for counter in range(1, 11):
    #print(counter, end=' ')

#for num in range(1000001):
    #total += num
#print("\n",total)

total = 0
grade_counter = 0
grades = [98,76,71,87,83,90,57,79,82,94]

for grade in grades:
    total += grade
    grade_counter += 1
print(total)
print(grade_counter)
average = total / grade_counter
print(f'average grade: {average}')