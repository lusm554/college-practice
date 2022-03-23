arrInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ESC = chr(27)

def find_max_replace(n):
    m = 0
    mi = 0
    for i in range(len(arrInt)):
        if arrInt[i] > m:
            m = arrInt[i]
            mi = i
    
    arrInt[mi] = int(n)
    print("Заменяем arrInt[{}]={} на {}".format(mi, m, n))
    

while 1:
    i = input("Введите число: ")

    if i == ESC:
        break
    
    find_max_replace(i)
    print(arrInt)
    print("Для выхода нажмите ESC\n")

