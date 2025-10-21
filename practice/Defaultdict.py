from collections import defaultdict

students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]
groups = defaultdict(list)
for student, group in students:
    groups[group].append(student)
 
print(groups)

# Если запрашиваемого ключа нет в словаре, KeyError не возникнет. Вместо этого будет
# напечатан пустой элемент, который создаётся в словаре по умолчанию:
print(groups[2021])

# Теперь в словаре groups автоматически появился элемент 2021 с пустым списком внутри,
# несмотря на то что мы его не создавали:
print(groups)