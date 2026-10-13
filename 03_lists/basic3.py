my_list = [1,2,3,4,5]

my_list.append(10)
print(my_list)

#Dobawlaem
my_list.insert(2, 1)
print(my_list)

#Udalenie
my_list.pop(0)
print(my_list)

deleted = my_list.pop(0)
print(f"my_list: {my_list}  | Deleted: {deleted}")

my_list.remove(10) #del po znaceniu
print(my_list)

#SORTIROWKA

my_list.sort(reverse=True)  # reverse=True mozno BEZ
print(my_list)