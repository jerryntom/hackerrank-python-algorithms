def getMoneySpent(keyboards, drives, b):
    options = list()

    for k in keyboards:
        for d in drives:
            sum_ = k + d
            if sum_ <= b:
                options.append(sum_)

    if len(options) == 0:
        return -1

    maxi = options[0]

    for o in options:
        if o > maxi:
            maxi = o

    return maxi


bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)