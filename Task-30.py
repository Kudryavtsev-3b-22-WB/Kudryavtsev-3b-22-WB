def letter_count(string):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    vow_count = 0
    con_count = 0
    el_count = 0
    res = []
    for i in string:
        if i in vowels:
            vow_count += 1
        elif i in consonants:
            con_count += 1
        else:
            el_count += 1


    res.append(vow_count)
    res.append(con_count)
    res.append(el_count)
    return res


count = letter_count(input('Ввод: '))
print(f"Гласных букв {count[0]}, согласных букв {count[1]}, других знаков {count[2]}")