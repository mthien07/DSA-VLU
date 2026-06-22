def insertion_sort_abs_stable(arr):
    a = arr.copy()
    n = len(a)
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and abs(a[j]) > abs(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
