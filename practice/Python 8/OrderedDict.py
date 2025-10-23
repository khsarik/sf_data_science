from collections import OrderedDict

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]

ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)
# По результатам 3 повторов получились вот такие результаты:
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])

# Сортируем по второму значению из кортежа, то есть по возрасту
ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1]))
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25)])

ordered_client_ages['Nikita'] = 18
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25), ('Nikita', 18)])

del ordered_client_ages['Andrey']
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18)])
ordered_client_ages['Andrey'] = 23
print(ordered_client_ages)
# OrderedDict([('Ivan', 19), ('Mark', 25), ('Maria', 20), ('Nikita', 18), ('Andrey', 23)])