def my_num(i):
    for i  in range(1, i + 1, 2):
        yield i

        
for y in my_num(9):
    print(y)
