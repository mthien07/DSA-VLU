def merge_count_inversions(arr):
    """Dem so nghich the (= so shift cua IS) trong O(n log n) bang merge sort"""
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_count_inversions(arr[:mid])
    right, inv_right = merge_count_inversions(arr[mid:])
    merged = []
    inversions = inv_left + inv_right
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

# Vi du voi mang lon
