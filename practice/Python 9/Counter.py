
""""Counter - считает количество элементов в объекте"""

from collections import Counter
 
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white'] 

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
 
print(counter_moscow)
print(counter_spb)

# Mojno pribavit' dva ob'yekta Counter.
print(counter_moscow + counter_spb)
print (counter_moscow - counter_spb) # ne budet otricatel'nix resul'tatov
# Otnimayem (wtobi posmotret' raznitsu).
#counter_moscow.subtract(counter_spb)
#print(counter_moscow)

""""Дополнительные функции"""

# 1 Чтобы получить список всех элементов, которые содержатся в Counter
print(*counter_moscow.elements())

# 2 Чтобы получить список уникальных элементов
print(list(counter_moscow))

# 3 С помощью функции dict() можно превратить Counter в обычный словарь:
print(dict(counter_moscow))

# 4 Функция most_common() позволяет получить список из кортежей элементов в порядке
# убывания их встречаемости:
print(counter_moscow.most_common())
print(counter_moscow.most_common(2))

# 5 Наконец, функция clear() позволяет полностью обнулить счётчик:
counter_moscow.clear()
print(counter_moscow)