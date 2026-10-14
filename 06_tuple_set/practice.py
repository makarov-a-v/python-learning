
student = ("Artsem", 32, "Python")

name, age, language = student

print(name)
print(age)
print(language)

print(name, age, language)

print(student)

words = ["python", "code", "list", "python", "set", "code", "tuple"] #У списка — .append(x)

unique_words = set(words)
print(len(unique_words))

print("tuple" in words) # or unique_words

unique_words.add("loop") #У множества — .add(x)
unique_words.remove("list") #.remove(x) — удаляет, если элемента нет → ошибка

#.discard(x) — удаляет, если элемента нет → не ошибка, тихо игнорирует

print(unique_words)
