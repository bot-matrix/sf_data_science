"""
Игра угадай число
компьютер сам загадывает и сам угадывает
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0

    while True:
        count +=1
        predict_number = np.random.randint(1, 101) #предполагаемое число
        if number == predict_number:
            break #выход из цикла если угадали

    return(count)

def score_game(rancom_predict) -> int:
    """за какое количество попыток угадывает в среднем

    Args:
        rancom_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size = (1000)) #загадали список чисел

    for number in random_array:
        count_ls.append(rancom_predict(number))

    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score

if __name__ == '__main__':
    #RUN
    score_game(random_predict)
