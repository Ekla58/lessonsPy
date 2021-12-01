def thesaurus(*args):
    my_dict = {}
    for y in sorted(args):
        idx = y[0]
        if idx in my_dict:
            my_dict[idx] += [y]
        else:
            my_dict[idx] = [y]

    return my_dict


print(thesaurus("Ольга", "Сергей", "Андрей", "Илья", "Инна", "Оксана", "Святослав"))
