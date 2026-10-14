author = {
    "name": "Artsem",
    "surname": "Makarov",
    "city": "Ashgabat",
    "age": 32
}


print(author['name'])
print(author.get("surname"))

author["city"] = "Minsk"
author["learning_python"] = True
author.pop("city") # Minsk
print(author)

#пригодится, когда при обработке данных нужно не только
#удалить поле, но и сохранить его значение.

for key, value in author.items():
    print(f"{key} — {value}")

