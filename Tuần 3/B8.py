def bubble_sort_sap_xep(a):
    n = len(a)
    if n <= 1:
        return a
    k = min(k, n-1)
    for i in range (k):
        swapped = False
        for j in range (0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            return True
    for i in range (n-1):
        return False
    return True