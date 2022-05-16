#!/usr/bin/env python3

import sys
from termcolor import colored
import pandas as pd

# 1
def ex1(salaries):
    res = sum(salaries) / len(salaries)
    print(f"Средняя зарплата: {res}")

def ex2(volume):
    pass

def main():
    ex = {
        "1": {
            "text": """Подсчитать среднемесячную зарплату сотрудника предприятия.""",
            "cb": ex1,
            "data": [50000, 76000, 20000, 40000, 122532]
        },
        "2": {
            "text": """Дан объем продукции, выпущенной заводом за год (помесячно). Найти наименьший объем. В качестве результата вывести номер месяца и объем выпущенной продукции.""",
            "cb": ex2,
            "data": []
        }
    }

    if len(sys.argv) > 1:
        n = sys.argv[1]
    else:
        n = input("Номер задания: ")
        print()

    if n in ex.keys():
        print(colored("Задание: ", 'green'))
        print(ex[n]["text"])

        print(colored("\nРешение: ", 'green'))
        ex[n]["cb"](ex[n]["data"])
    else:
        print(colored("Not found.", 'red', attrs=["underline"]))


if __name__ == "__main__":
    main()

