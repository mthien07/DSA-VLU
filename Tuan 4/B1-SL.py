def find_min_swap_first(a):
    n = len(a)
    min_idx = 0
    for i in range (1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    a[0], a[min_idx] = a[min_idx], a[0]
    return a
