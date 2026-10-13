city = 'moscOw'

#методы строк
#метод функции отличия+
#лен - можем передать любое значение в моём случае строку.
#а метод на основе какого то обьекта
len(range(5)) #сюда можем передать любой другой обьект, т.е любой другой тип данных. который поддерживается функцией len

print(city.capitalize()) #есть только у строк


print(city.lower())
print(city.upper())

phone_number = '+91123456789  '
if phone_number.strip().startswith('+9'):  #проверка начала # strip убирает пробелы
    print('Russian number')
else:
    print('Uknown')

print(phone_number.endswith('789')) #проверка конца


print(phone_number.replace('+911', '+999'))  #replace = zamena
print(phone_number.count('9'))
