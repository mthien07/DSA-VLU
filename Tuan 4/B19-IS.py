def gnome_sort(arr):
    a = arr.copy()
    n = len(a)
    ops = 0
    i = 0
    while i < n:
        if i == 0 or a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            ops += 1
            i -= 1
    return a, ops

def insertion_sort_count_ops(arr):
    a = arr.copy()
    n = len(a)
    ops = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            ops += 1
        a[j + 1] = key
    return a, ops
