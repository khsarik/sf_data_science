"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        
    Changes in code:
        - Получение предпологаемого числа было переписано таким образом, что при каждой
        итерации, предпологаемое число - это среднее суммы числа начала и конца диапозона.
        Таким образом, у нас станет значительно меньше попыток угадывания с 1-3 раз, но
        также станет меньше среднее количество попыток угадывания числа для всей выборки.
        - Цикл был переписан таким образом, чтобы после каждой итерации диапоазон
        предпологаемого числа становился меньше с конца или с начала в зависимости от
        того больше или меньше предрологаемое число загаданного. 
        - num_1, num_2 - начальное и конечное число для диапазона предпологаемого числа,
        соответственно.
    """
    count = 0
    num_1 = 1 # начальное число диапозона
    num_2 = 101 # клнечное число диапозона

    while True:
        count += 1
        predict_number = (num_1 + num_2) // 2   # предполагаемое число
        
        if number > predict_number:
            num_1 = predict_number + 1
        
        elif number < predict_number:
            num_2 = predict_number
    
        else:
            break #конец угадывания, выход из цикла
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
