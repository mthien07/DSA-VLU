def shell_sort(arr, gaps):
    a = arr.copy()
    n = len(a)
    total_shift = 0
    for gap in gaps:
        for i in range (gap, n):
            key = a[i]
            j = i
            while j >= gap and a[j - gap] > key:
                a[j] = a[j - gap]
                j -= gap
                total_shift += 1
            a[j] = key
    return a, total_shift

def insertion_sort_count(arr):
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
    return a, shift
