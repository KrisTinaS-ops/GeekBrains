names = {"А": ["Анжелика", "Алексей", "Андрей", "Алина"],
         "Б": ["Борис", "Богдан"],
         "И": ["Иван", "Илья", "Игорь", "Ибрагим"],
         "Н": ["Никита", "Наталия", "Наталья"]}


def thesaurus(*names):
    names_dict = dict()
    for name in names:
        names_dict.setdefault(name[0], [])
        names_dict[name[0]].append(name)
    return names_dict


print(thesaurus("Анжелика", "Ибрагим", "Никита", "Игорь"))
