
def insertion_sort_analysis(arr):
    a = arr.copy()
    n = len(a)
    so_sanh = 0
    shift = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            so_sanh += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
                shift += 1
            else:
                break
        a[j + 1] = key
    return so_sanh, shift
