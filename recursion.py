def rec(num):
    print(num)
    if num == 100:
        return "One hundred"
    else:
        return rec(num + 1)


rec(1)
