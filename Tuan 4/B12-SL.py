def stable_selection_sort(arr):
    """Selection sort on dinh: dich chuyen thay vi swap"""
    a = arr.copy()
    n = len(a)
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
        # Dich chuyen phan tu min ve vi tri i (khong swap)
        min_val = a[min_idx]
        for k in range (min_idx, i, -1):
            a[k] = a[k - 1]
        a[i] = min_val
    return a
