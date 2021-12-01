my_dict = {"zero": "ноль", "one": "один",
           "two": "два", "three": "три",
           "four": "четыре", "five": "пять",
           "six": "шесть", "seven": "семь",
           "eight": "восемь", "nine": "девять",
           "ten": "десять"}


def trans(word):
    return my_dict.get(word)


print(trans(input("Введите число от 0 до 10 на английском: ")))