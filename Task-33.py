def count(string):
    result = {}
    unique = set(string)
    for i in unique:
        result[i] = string.count(i)
    return result

print(count(input("Введите строку для подсчета символов: ")))