translate = {'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def num_translate_adv(late):
    if late[0] == late[0].upper():
        eng = late.lower
        return translate[eng].capitalize()
    else:
        return translate[late]


print(num_translate_adv(input('Напишите число: ')))
