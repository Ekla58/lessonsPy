cube_list=[]
new_cube_list=[]
sum=0
for i in range(1000):
    if i%2:
        cube_list.append(i**3)
for idx, item in enumerate(cube_list):
    sum_num=0
    while item>0:
        sum_num+=item%10
        item//=10
    if sum_num%7==0:
        sum+=cube_list[idx]
print(sum)

for n in cube_list:
    new_cube_list.append(n+17)

sum=0

for idx, item in enumerate(new_cube_list):
    sum_num=0
    while item>0:
        sum_num+=item%10
        item//=10
    if sum_num%7==0:
        sum+=new_cube_list[idx]
print(sum)