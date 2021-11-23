num=int(input("Введите количество секунд: "))
if 0<num<60:
    print(num, "сек")
if 60<=num<3600:
    min=num//60
    sec=num%60
    print(min, "мин", sec, "сек")
if 3600<=num<86400:
    hour=num//3600
    min=(num%3600)//60
    sec=(num%3600)%60
    print(hour, "час", min, "мин",sec, "сек")
if 86400<=num:
    day=num//86400
    hour=(num%86400)//3600
    min=(num%3600)//60
    sec=num%60
    print(day, "дн", hour, "час", min, "мин", sec, "сек")