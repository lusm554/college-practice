#!/usr/bin/env python3

import sys
from termcolor import colored

# 1
def ex1():
    gb_to_mb = lambda gb: gb * 1024
    card_volume = gb_to_mb(8)
    try:
        img_volume = float(input("Введите размер фотографии в Мбайтах(8, 8.2, ...): "))
    except Exception:
        print("Invalid input.")
    else:
        print(f"Поместится фотографий: {card_volume // img_volume}.")

# 2
def ex2():
    khz = 44.1
    deep = 24
    V = lambda M, I, t: M * I * t
    min_to_sec = lambda m: m * 60
    khz_to_hz = lambda khz: khz * 1000

    try:
        t_min = int(input("Введите время записи в минутах: "))
        t_sec = min_to_sec(t_min)
    except Exception:
        print("Invalid input.")
    else:
        v = V(M=khz_to_hz(khz), I=deep, t=t_sec) / (8 * 10**6)
        print(f"Размер файла – {v} Мбайт.")

# 3
def ex3():
    pass 


def main():
    ex = {
    "1": {
        "text": """Ввести число, обозначающее размер одной фотографии в Мбайтах. Определить, сколько фотографий поместится на флэш-карту объёмом 8 Гбайта.""",
        "cb": ex1

    },
    "2": {
        "text": """Оцифровка звука выполняется в режиме стерео с частотой дискретизации 44,1 кГц и глубиной кодирования 24 бита. Ввести время записи в минутах и определить, сколько Мбайт нужно выделить для хранения полученного файла (округлить результат в большую сторону).""",
        "cb": ex2
    },
    "3": {
        "text": """Разведчики-математики для того, чтобы опознать своих, используют числовые пароли. Услышав число-пароль, разведчик должен возвести его в квадрат и сказать в ответ первую цифры дробной части полученного числа. Напишите программу, которая по полученному паролю (вещественному числу) вычисляет число-ответ.""",
        "cb": ex3
        }
    }

    if len(sys.argv) > 1:
        n = sys.argv[1]
    else:
        n = input("Номер задания(1, 2, 3): ")
        print()

    if n in ["1", "2", "3"]:
        print(colored("Задание: ", 'green'))
        print(ex[n]["text"])

        print(colored("\nРешение: ", 'green'))
        ex[n]["cb"]()
    else:
        print(colored("Not found.", 'red', attrs=["underline"]))


if __name__ == "__main__":
    main()
