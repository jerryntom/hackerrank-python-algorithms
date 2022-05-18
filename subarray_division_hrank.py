def birthday(s, d, m):
    x = 0

    for i in range(0, (len(s) + 1 - m)):
        sum_ = 0
        dl = 0
        for j in range(i, i+m):
            sum_ += s[j]
            dl += 1
            if dl == m:
                if sum_ == d:
                    x += 1
                break

    return x


s = list(map(int, input().rstrip().split()))
first_multiple_input = input().rstrip().split()
d = int(first_multiple_input[0])
m = int(first_multiple_input[1])

print(birthday(s, d, m))
