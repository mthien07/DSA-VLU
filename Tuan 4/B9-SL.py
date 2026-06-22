def double_selection_sort(arr):
    a = arr.copy()
    n = len(a)
    so_sanh = 0
    left = 0
    right = n - 1
    while left < right:
        min_idx = left
        max_idx = left
        for i in range (left, right + 1):
            so_sanh += 1
            if a[i] < a[min_idx]:
                min_idx = i
            so_sanh += 1
            if a[i] > a[max_idx]:
                max_idx = i
        a[left], a[min_idx] = a[min_idx], a[left]
        if max_idx == left:
            max_idx = min_idx
        a[right], a[max_idx] = a[max_idx], a[right]
        left += 1
        right -= 1
    return a, so_sanh

def selection_sort_count(arr):
    a = arr.copy()
    n = len(a)
    so_sanh = 0
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, so_sanh
