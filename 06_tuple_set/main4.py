#множества - уникальность объектов.

#numbers = {100, 102, 103, 104, 105}

#languages = {"Python", "Java", "C++", "C", "Java"}
#print(languages) #{'Python', 'Java', 'C', 'C++'}

languages = ["Python", "Java", "C++", "C", "Java"]
print(languages)

unique_languages = set(languages) #set - cоздание множества дубликаты уйдут
print(unique_languages) #{'C++', 'Java', 'Python', 'C'}
