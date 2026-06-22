
def insertion_sort_stats(arr):
    a = arr.copy()
    so_sanh = shift = 0
    for i in range (1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            so_sanh += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
                shift += 1
            else:
                break
        a[j + 1] = key
    return so_sanh, shift

def bubble_sort_stats(arr):
    a = arr.copy()
    so_sanh = swap = 0
    n = len(a)
    for i in range (n):
        swapped = False
        for j in range (0, n - i - 1):
            so_sanh += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swap += 1
                swapped = True
        if not swapped:
            break
    return so_sanh, swap

def selection_sort_stats(arr):
    a = arr.copy()
    so_sanh = swap = 0
    n = len(a)
    for i in range (n):
        min_idx = i
        for j in range (i + 1, n):
            so_sanh += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swap += 1
    return so_sanh, swap
