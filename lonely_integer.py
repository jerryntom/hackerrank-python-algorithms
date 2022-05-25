def lonelyinteger(a):
    values = [num for num in a]
    set_values = set(values)
    counter = {num: 0 for num in values}

    for num in values:
        counter[num] += 1

    for k, v in counter.items():
        if v == 1:
            return k


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))
