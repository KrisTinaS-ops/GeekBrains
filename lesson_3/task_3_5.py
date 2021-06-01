import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    jokes_list = []
    """
    Задокументировала код функции
    """
    for i in range(num):
        nouns_1 = random.choice(nouns)
        adverbs_1 = random.choice(adverbs)
        adjectives_1 = random.choice(adjectives)
        jokes_list.append(f'{nouns_1} {adverbs_1} {adjectives_1}')
    return jokes_list


print(get_jokes(1))
print(get_jokes(3))
