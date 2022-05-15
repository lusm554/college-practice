#!/usr/bin/env python3

import sys
from termcolor import colored

# 1
def ex1():
    v = ["кг", "граммы", "тонны", "центнер", "миллиграммы", "унции"] 
    val = int(input("Введите значение: "))
    fr = input(f"Из {', '.join(v)}: ").strip()
    to = input(f"В {', '.join(v)}: ").strip()

    assert fr in v and to in v, 'Not valid unit.'

    if fr == "кг":
        if to == "кг":
            print(val)
        elif to == "граммы":
            print(val * 1000)
        elif to == "тонны":
            print(val / 1000)
        elif to == "центнер":
            print(val / 10)
        elif to == "миллиграммы":
            print(val * 1e6)
        elif to == "унции":
            print(val * 35.274)

# 2
def ex2():
    pass

# 3
def ex3():
    pass

# 4
def ex4():
    pass


def main():
    ex = {
        "1": {
            "text": """Перевод веса из кг в граммы, тонны, центнер, миллиграммы, унциии наоборот.""",
            "cb": ex1
        },
        "2": {
            "text": """Перевод расстояния из км в метры, дециметры, сантиметры, миллиметры, мили и наоборот.""",
            "cb": ex2
        },
        "3": {
            "text": """Перевод времени из года в месяцы, недели, сутки, часы, минуты и наоборот.""",
            "cb": ex3
        },
        "4": {
            "text": """Перевод температуры из градусов Цельсия в градусы Фаренгейта, Кельвины, градусы Реомюра и наоборот.""",
            "cb": ex4
        }
    }


    if len(sys.argv) > 1:
        n = sys.argv[1]
    else:
        n = input("Номер задания(1..4): ")
        print()

    if n in ex.keys():
        print(colored("Задание: ", 'green'))
        print(ex[n]["text"])

        print(colored("\nРешение: ", 'green'))
        ex[n]["cb"]()
    else:
        print(colored("Not found.", 'red', attrs=["underline"]))


if __name__ == "__main__":
    main()

