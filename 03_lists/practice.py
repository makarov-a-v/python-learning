'''#Задача 1
numbers = [12, 5, 8, 99, 3, 8]

print(numbers[0], numbers[-1])

print("do have num 8: ",  8 in numbers)
print(f'Summ {sum(numbers)} \nMin {min(numbers)} | Max {max(numbers)}')


##Задача 2
gods = ['Zeus', 'Apollo', 'Ares']

gods.append("Hermes")
gods.insert(1, "Hades")
gods.remove('Apollo')

gods_del = gods.pop()


print(f'Итоговый список: {gods} | Удаленный элемент: {gods_del}')


##Задача 3
numbers = [4, 7, 10, 15, 18, 21, 24]
for i in numbers:
    print(i)

even_numbers = [i for i in numbers if i % 2 == 0]
print(even_numbers)

for index, element in enumerate(numbers):
    print(index, element)

count = 0
for num in numbers:
    if num > 10:
        count += 1
print(count)

#Задача 4
string = input()
my_list = string.split()
print(my_list)

string = '-'.join(my_list)
print(string)


#Задача 5
spis_kw = [i ** 2 for i in range(1, 11) if not i % 3 == 0] #i % 3 != 0
print(spis_kw)

'''

numbers = [2, 4, 6]
result = [x * 2 for x in numbers if x > 3]
print(result)