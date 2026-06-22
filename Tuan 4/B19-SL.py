def double_selection_sort_safe(arr):
    """Double selection sort xu ly truong hop bien"""
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
        # Swap min ve dau
        a[left], a[min_idx] = a[min_idx], a[left]
        # Truong hop bien: neu max_idx == left thi max da bi doi sang min_idx
        if max_idx == left:
            max_idx = min_idx
        # Swap max ve cuoi
        a[right], a[max_idx] = a[max_idx], a[right]
        left += 1
        right -= 1
    return a, so_sanh
