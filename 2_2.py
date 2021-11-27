my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_my_list = []
for y in my_list:
    if y.replace("+", "").replace("-", "").isdigit():
        if y.isdigit():
            new_my_list.append(f"'{int(y):02}'")
        else:
            new_my_list.append(f"'{y[0]}{int(y[1:]):02}'")
    else:
        new_my_list.append(y)
print(new_my_list)
print(" ".join(new_my_list))