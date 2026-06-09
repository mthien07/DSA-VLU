def bubble_sort_one_pass(a):
    n = len(a)
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    return a