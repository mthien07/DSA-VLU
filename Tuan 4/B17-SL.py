def kth_smallest(arr, k):
    """Tim phan tu nho thu k bang partial selection sort"""
    a = arr.copy()
    n = len(a)
    for i in range (k):
        min_idx = i
        for j in range (i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[k - 1]
