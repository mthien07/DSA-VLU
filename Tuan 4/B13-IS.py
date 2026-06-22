def insertion_sort_stable(arr):
    """Sap xep theo khoa (phan tu dau), giu nguyen thu tu neu cung khoa"""
    a = arr.copy()
    n = len(a)
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
