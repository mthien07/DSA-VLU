def count_inversions(arr):
    """Dem so nghich the cua mang"""
    inv = 0
    n = len(arr)
    for i in range (n):
        for j in range (i + 1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv

def insertion_sort_count_shift(arr):
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
