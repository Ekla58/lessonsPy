
price_list = [49.78, 74.20, 63, 12.3, 59.99, 58.3, 68.78,
              41, 11.3, 25.1, 25, 86.7, 65.01, 45, 65.25, 74.3, 24.09]
for n in price_list:
    rub, kop = f"{n:.2f}".split(".")
    print(f"{rub} руб {kop} коп,", end=" ")

print(f"\n{'='*20}")

print(f"ID: {id(price_list)} - {price_list}")
price_list.sort()
print(f"new ID: {id(price_list)} - {price_list}")

print(f"\n{'+'*20}")

new_price_list = sorted(price_list, reverse=True)
print(f"new ID: {id(new_price_list)} - {new_price_list}\n{new_price_list[:5][::-1]}")