def selection_sort_swap(arr):
    a = arr.copy()
    n = len(a)
    swap = 0
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1
    return swap

def bubble_sort_swap(arr):
    a = arr.copy()
    n = len(a)
    swap = 0
    for i in range (n):
        for j in range (0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
    return swap

# So sanh
