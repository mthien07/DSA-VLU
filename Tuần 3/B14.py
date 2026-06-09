def cocktail_shaker_sort(arr):
    a = arr.copy()
    n = len(a)
    so_luot = 0
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        so_luot += 1
        for i in range(start, end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        end = end - 1 
        swapped = False
        so_luot += 1
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1 
    return a, so_luot