

'''message = input("Enter your message: ")

message = message.strip()

if not message:
    print("EMPTY")
elif "spam" in message.lower():
    print("BLOCKED")
else:
    print(message)
'''

'''s = input("Enter your message: ")
i = int(input("Enter your number: "))

if 0 <= i < len(s):
    char = s[i]
    print(char)
    print(char.lower() == "a")
else:
    print('IndexError')'''

'''full_name = input("Enter your full name: ")

full_name = full_name.strip().capitalize()

print(f'{full_name[0]}.{full_name[-1]}')'''

#Пользователь вводит число n. Выведи все числа от n до 1 в обратном порядке

'''n = int(input("Enter your number: "))
for i in range(n, 0, -1):
    print(i)'''

#Пользователь вводит числа, пока не введёт 0. Найди количество введённых чисел (без нуля)



'''summ = 0
while True:
    n = int(input())
    if n == 0:
        break
    summ += 1
print(summ)'''


'''message = input("Enter your message: ")

message = message.strip().lower()
if "a" in message:
    print("Есть a")
else:
    print("Нет a")'''


'''numbers = input("Enter your numbers: ")
product = 1

for i in numbers:     #произведение его цифр
    product *= int(i)
print(product)
'''

numbers = input("Enter your numbers: ")

if numbers == numbers[::-1]:
    print("палиндром")
else:
    print("не палиндром")