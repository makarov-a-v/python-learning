'''language = input('Input your favorite language: ')

if language == 'Python':
    print('True')
else:
    print('False')
'''

age = 20
language = 'Python'

print(language == 'Python' and not age< 18)
if age < 18:
    print('Dostup zapresen')
elif age > 18 and age < 99:
    print('Go in')
elif age > 99:
    print('u r old')
else:
    print('u have 18 y.')
