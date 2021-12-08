src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

my_dict = {y: 0 for y in src}

for y in src:
    my_dict[y] += 1

print([y for y in my_dict if my_dict[y] == 1])
