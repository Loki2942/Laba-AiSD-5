"""
Лабораторная работа №5
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления
данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по
лабораторной работе.

Вариант №16

F(1) = 1; G(1) = 1; F(n) = 2*F(n–1) – G(n–1), G(n) = 2*F(n–1) // G(n–1), при n >=2
"""


import time
import matplotlib.pyplot as plt


def recursive_f(n):  # рекурсивное решение
    if n == 2:
        return 1
    else:
        return 2 * recursive_f(n - 1) + recursive_g(n - 1)


def recursive_g(n):  # рекурсивное решение
    if n == 2:
        return 1
    else:
        return 2 * recursive_f(n - 1) // recursive_g(n - 1)


def iterative_f(n):
    gn = [1] * (n + 1)
    fn = [1] * (n + 1)
    for i in range(3, n + 1):
        fn[i] = 2 * fn[i - 1] + gn[i - 1]
        gn[i] = 2 * fn[i - 1] // gn[i - 1]
    return fn[n]

try:
    print("Введите натуральное число n >=2")
    n = int(input())
    while n < 2:  # ошибка в случае введения не натурального числа
        n = int(input("\nВы ввели число меньше 2"))

    k = 1
    if n > 25:
        k = int(input(
            "\nЧисло n > 25. Хотите продолжить ? Это может занять существенное время. (Да: 1 / Нет: 0):\n"))
    while k != 0 and k != 1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу:\n"))

    if k == 1:

        recursive_times = []  # создание списков для дальнейшего построения таблицы
        recursive_values = []
        iterative_times = []
        iterative_values = []
        n_values = list(range(2, n + 1))

        for n in n_values:  # заполнение списков данными

            start = time.time()
            recursive_values.append(recursive_f(n))
            end = time.time()
            recursive_times.append(end - start)

            start = time.time()
            iterative_values.append(iterative_f(n))
            end = time.time()
            iterative_times.append(end - start)

        table_data = []  # создание и заполнение последующей таблицы
        for i, n in enumerate(n_values):
            table_data.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])

        print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)',
                                                         'Значение рекурсии', 'Значение итерации'))  # вывод таблицы
        print('-' * 105)
        for data in table_data:
            print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))

        plt.plot(n_values, iterative_times, label='Итерация')
        plt.plot(n_values, recursive_times, label='Рекурсия')  # вывод графиков
        plt.xlabel('n')
        plt.ylabel('Время (с)')
        plt.title('Сравнение рекурсивного и итерационного подхода')
        plt.legend()
        plt.show()

    print("\nРабота программы завершена.\n")
except ValueError:
    print("\nВы ввели число, не следуя условиям. Перезапустите программу и введите число, следуя инструкциям.")

except RecursionError:
    print("\nВы превысили относительную максимальную глубину рекурсии.")
