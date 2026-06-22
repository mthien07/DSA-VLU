def insertion_sort_right_to_left(arr):
    """Do tu phai sang trai (chuan)"""
    a = arr.copy()
    so_sanh = 0
    for i in range (1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            so_sanh += 1
            a[j + 1] = a[j]
            j -= 1
        if j >= 0:
            so_sanh += 1  # lan so sanh cuoi (a[j] <= key)
        a[j + 1] = key
    return a, so_sanh

def insertion_sort_left_to_right(arr):
    """Do tu trai sang phai"""
    a = arr.copy()
    so_sanh = 0
    for i in range (1, len(a)):
        key = a[i]
        # Tim vi tri chen tu trai sang phai
        pos = 0
        while pos < i:
            so_sanh += 1
            if a[pos] > key:
                break
            pos += 1
        # Dich chuyen va chen
        for j in range (i, pos, -1):
            a[j] = a[j - 1]
        a[pos] = key
    return a, so_sanh
