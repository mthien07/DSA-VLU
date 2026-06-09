def bubble_sort_early_exit(a):
    n = len(a)
    if n <= 1:
        return a
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a