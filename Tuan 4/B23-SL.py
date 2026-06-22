
def selection_sort_analysis(arr):
    a = arr.copy()
    n = len(a)
    so_sanh = 0
    swap = 0
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1
    return so_sanh, swap
