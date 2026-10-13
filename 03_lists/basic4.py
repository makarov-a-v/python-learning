numbers = [0, 1, 2, 3, 4, 5]

for i in numbers: #i peremennaya cikla kot prin konkr znac,
    print(i)

languages = ['Python', 'JavaScript', 'Java']

for index, element in enumerate(languages):
    print(index, element)

languages = ['Python', 'JavaScript', 'C#']

for index, element in enumerate(languages):
    print(index, element)

languages.insert(1, 'C++')
print(languages)