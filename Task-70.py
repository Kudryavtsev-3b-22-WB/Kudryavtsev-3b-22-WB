def find_intersection(list1, list2):
    # Преобразуем списки во множества для удобства нахождения пересечения
    set1 = set(list1)
    set2 = set(list2)

    # Находим пересечение множеств
    intersection = set1.intersection(set2)

    return list(intersection)

def main():
    try:
        # Вводим два списка чисел
        list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))
        list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

        # Проверяем, что списки содержат не менее трех элементов
        if len(list1) < 3 or len(list2) < 3:
            print("Списки должны содержать не менее трех элементов.")
            return

        # Находим пересечение списков
        intersection = find_intersection(list1, list2)

        if intersection:
            print("Пересечение списков:", intersection)
        else:
            print("Пересечения нет.")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа через пробел.")

if __name__ == "__main__":
    main()
