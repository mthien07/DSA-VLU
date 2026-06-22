def insertion_sort_count_comparisons(arr):
    a = arr.copy()
    n = len(a)
    so_lan_so_sanh = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            so_lan_so_sanh += 1
            if key < a[j]: 
                a[j + 1] = a[j] 
                j -= 1
            else:
                break
        a[j + 1] = key
    return so_lan_so_sanh, a
