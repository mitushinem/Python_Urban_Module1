# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = (1, 14.3, [1,2,3,4,5], ['a', 'b', 'c', 'd', 'e'], 'abc')
print(immutable_var)

immutable_var[2].append(10)
print(immutable_var)
# Изменить можно только элемент с изменяемым типом данных, добавить или удалить нельзя

mutable_list = [1,2,3,4,5]
mutable_list.extend([[6,7],'7',True,9])
mutable_list.append('22')
print(mutable_list)