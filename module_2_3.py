my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
s = 0
a = int(my_list[s])
b=len(my_list)
while s < b:
    a = int(my_list[s])
    if a > 0:
        print(a)
        s += 1
        continue
    elif a == 0:
        s += 1
        continue
    else:
        break


