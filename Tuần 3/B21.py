def bubble_sort_stable(a):
    a = a.copy()
    n = len(a)
    for i in range (n-1):
        swapped = False
        for j in range (0, n -i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def bubble_sort_unstable(a):
    a = a.copy()
    n = len(a)
    for i in range (n-1):
        min_idx = i
        for j in range (i-1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[j], a[min_idx] = a[min_idx], a[j]
    return a

