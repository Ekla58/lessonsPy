from itertools import islice, zip_longest

tutors = ["Иван", "Анастасия", "Петр", "Сергей", "Дмитрий", "Борис", "Елена"]
klass = ["9А", "7В", "9Б", "9В", "8Б", "10А", "10Б", "9А"]

res = (n for n in zip_longest(tutors, klass))

print(type(res))
print(*islice(res, 9))
print(list(islice(res, 3)))
