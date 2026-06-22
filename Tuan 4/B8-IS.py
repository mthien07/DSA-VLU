def insertion_sort_k_steps(arr, k):
    a = arr.copy()
    n = len(a)
    so_buoc = min(k + 1, n) 
    for i in range (1, so_buoc):
        key = a[i] 
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
