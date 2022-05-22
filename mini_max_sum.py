def miniMaxSum(arr):
    mini_sum = 0
    max_sum = 0

    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    for i in range(0, len(arr)):
        if i < len(arr) - 1:
            mini_sum += arr[i]
        if i > 0:
            max_sum += arr[i]

    print(mini_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
