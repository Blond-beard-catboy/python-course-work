from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Настройте контекст и подготовьте вызов указанного Алгоритма
    # с использованием предоставленного массива. Только импортировать
    # функция алгоритма, если это не встроенная функция sorted()
    setup_code = f"from __main__ import {algorithm}" \
    if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Выполнить код десять раз и каждый раз
    # вернуть время в секундах
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Наконец, покажите название алгоритма и
    # минимальное время, необходимое для его выпонения
    print(f"Алгоритм: {algorithm}. Минимальное время исполнения: {min(times)}")
