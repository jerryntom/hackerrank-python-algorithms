def utopianTree(n):
    h = 1

    for i in range(1, n + 1):
        if i % 1 == 0 and i % 2 != 0:
            h *= 2
        else:
            h += 1

    return h


print(utopianTree(5))
