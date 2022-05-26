def countingSort(arr):
    maxi = max(arr)

    count_array = [0 for x in range(0, maxi + 1)]

    for element in arr:
        count_array[element] += 1

    for value in count_array:
        pass

    if len(count_array) < 100:
        for i in range(0, 100 - len(count_array)):
            count_array.append(0)

    return count_array


print(countingSort([1, 2, 3, 3, 2, 1, 5, 6, 0, 3, 2, 1]))
