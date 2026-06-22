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
    return so_sanh

def heap_sort_count(arr):
    a = arr.copy()
    n = len(a)
    so_sanh = 0

    def heapify(n, i):
        nonlocal so_sanh
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n:
            so_sanh += 1
            if a[l] > a[largest]:
                largest = l
        if r < n:
            so_sanh += 1
            if a[r] > a[largest]:
                largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(n, largest)

    for i in range (n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range (n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(i, 0)
    return so_sanh

# So sanh
