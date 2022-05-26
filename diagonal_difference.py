def diagonalDifference(arr):
    primary = arr[0][0]
    secondary = arr[0][len(arr) - 1]

    for i in range(1, len(arr)):
        primary += arr[i][i]

    for j in range(1, len(arr)):
        i -= 1
        secondary += arr[j][i]

    return abs(primary - secondary)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(diagonalDifference(arr))
