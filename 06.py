# Практическое задание по теме: "Списки и словари"

my_list = ['banana', 'apple', 'orange', 'pear', 'kiwi', 'strawberry', 'blueberry']
print(my_list)
print('First element:', my_list[0])
print('Last element:', my_list[-1])
print(my_list[2:5])
my_list[2] = 'mango'
print('Modified list: ', my_list)

my_dict = {'apple': 'яблоко', 'banana': 'банан', 'orange': 'апельсин'}
print(my_dict)
print(my_dict['orange'])
# my_dict.setdefault('kiwi', 'киви')
my_dict['kiwi'] = 'киви'
print(my_dict)
