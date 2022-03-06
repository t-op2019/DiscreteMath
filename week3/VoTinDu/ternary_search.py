def ternary_search(array, left, right, n):
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if array[mid1] == n:
            return mid1
        if array[mid2] == n:
            return mid2

        if array[mid1] > n:
            return ternary_search(array, left, mid1 - 1, n)
        elif array[mid2] < n:
            return ternary_search(array, mid2 + 1, right, n)
        else:
            return ternary_search(array, mid1 + 1, mid2 - 1, n)

    return -1


array = [1, 4, 6, 7, 9, 12, 14, 16, 17, 27, 30]
left = 0
right = len(array) - 1

n = 27

print(ternary_search(array, left, right, n))
