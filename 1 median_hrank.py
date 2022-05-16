def findMedian(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[j] > arr[i]:
                pom = arr[i]
                arr[i] = arr[j]
                arr[j] = pom

    if len(arr) % 2 != 0:
        return arr[len(arr)//2]
    else:
        median = arr[(len(arr)//2) - 1] + arr[(len(arr)//2)]
        median /= 2

    return median


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    print(result)
