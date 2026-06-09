def bubble_sort_min_passes(a):
    arr = a.copy()
    n = len(arr)
    so_luot = 0
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped:
            so_luot += 1
        else:
            break
    return so_luot
