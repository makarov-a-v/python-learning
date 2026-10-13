#Как удобно в одну строку удобно и гибко создавать строку
#Списочные выражения (list comprehension)

numbers = []
for i in range(6):
    numbers.append(i)

print(numbers)

numbers = [i for i in range(7) if i % 2 == 0] # И добавлять условия: # только четные
print(numbers)

# Можно усложнять различными выражениями:
numbers = [i * 2 for i in range(7)]
print(numbers)


# Еще примеры для закрепления:
word = 'Hello'
numbers = [1, 14, 5, 9, 12]
words = ['one', 'two', 'three', 'four', 'five', 'six']

#Списочное выражение	Результирующий список
#[c * 2 for c in word]	['HH', 'ee', 'll', 'll', 'oo']
#[m[0] for m in words]	['o', 't', 't', 'f', 'f', 's']
#[i for i in numbers if i < 10]	[1, 5, 9]
#[m[0] for m in words if len(m) == 3]	['o', 't', 's']
