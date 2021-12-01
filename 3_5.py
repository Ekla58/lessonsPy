from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(i, repeat=False):
    """
    :param i: колличество шуток
    :param repeat: уникальные/неуникальные
    :return: список случайных шуток
    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_j = []
    list_min = min(no, adv, adj)

    while i and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        i -= 1
    return list_j


print(some_jokes(8, True))
