from math import inf

def divide(first, second):
    # Возвращает деление с остатк

    if second == 0:
        return inf
    return first / second


    # Ввод данных от пользователя


# first = int(input())                            #"Введите делимое: "
# second = int(input())                           #"Введите делитель: "
#
# remainder = divide(first, second)
#
# print(f' {remainder}')                  #Результат
# print()