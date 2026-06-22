def binary_search_pos(a, key, start, end):
    so_sanh = 0
    while start <= end:
        mid = (start + end) // 2
        so_sanh += 1
        if key < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start, so_sanh

def binary_insertion_sort(arr):
    a = arr.copy()
    n = len(a)
    tong_ss_binary = 0
    tong_shift = 0
    for i in range (1, n):
        key = a[i]
        pos, ss = binary_search_pos(a, key, 0, i - 1)
        tong_ss_binary += ss
        for j in range (i, pos, -1):
            a[j] = a[j - 1]
            tong_shift += 1
        a[pos] = key
    return a, tong_ss_binary, tong_shift

def normal_insertion_sort(arr):
    a = arr.copy()
    n = len(a)
    tong_ss = 0
    tong_shift = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            tong_ss += 1
            if key < a[j]:
                a[j + 1] = a[j]
                j -= 1
                tong_shift += 1
            else:
                break
        a[j + 1] = key
    return a, tong_ss, tong_shift
