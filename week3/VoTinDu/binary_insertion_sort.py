def binary_search(arr, left, right, x):
    if right == left:
        if arr[left] > x:
            return left
        else:
            return left + 1

    if right < left:
        return left

    mid = (right + left) // 2
    if arr[mid] == x:
        return mid

    if arr[mid] > x:
        return binary_search(arr, left, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, right, x)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        insertAt = binary_search(arr, 0, j, val)
        while j >= insertAt:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val

    return arr


arr = [1, 5, 4, 6, 3, 4, 5, 89, 7, 0]

print(insertion_sort(arr))
