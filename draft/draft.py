import numpy as np

def shuffle_seed(array):
    # 1. Генерируем случайный seed в нужном диапазоне
    seed = np.random.randint(0, 2**32, dtype=np.int64)
    
    # 2. Создаем копию массива, чтобы не изменять исходный (как требует условие)
    # Использование np.array() по умолчанию делает копию
    arr_copy = np.array(array)
    
    # 3. Инициализируем генератор случайных чисел нашим seed
    np.random.seed(seed)
    
    # 4. Перемешиваем массив (in-place)
    np.random.shuffle(arr_copy)
    
    # 5. Возвращаем кортеж из перемешанного массива и seed
    return arr_copy, seed

# Проверка:
array = [1, 2, 3, 4, 5]
print(shuffle_seed(array))
# Исходный array остался [1, 2, 3, 4, 5]