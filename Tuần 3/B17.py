def bubble_sort_k_pass(a, k):
    n = len(a)
    if n <= 1 or k <= 0:
        return a
    k = min(k, n-1)
    for i in range (k):
        swapped = False
        for j in range (0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a
