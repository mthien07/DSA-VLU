import random

def insertion_sort_count(arr):
    a = arr.copy()
    n = len(a)
    shift = 0
    for i in range (1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            shift += 1
        a[j + 1] = key
    return shift

def generate_k_sorted(n, k):
    """Tao mang ma moi phan tu cach vi tri dung toi da k"""
    a = list(range (n))
    for i in range (n):
        j = min(i + random.randint(0, k), n - 1)
        a[i], a[j] = a[j], a[i]
    return a
