def count_shift_insertion_sort(arr):
    a = arr.copy()
    n = len(a)
    shift = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shift += 1
        a[j + 1] = key
    return shift, a
