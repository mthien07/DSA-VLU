def bubble_sort_ptucuoi(a):
    n = len(a)
    if n == 0:
        return None
    for i in range (n-1):
        if a[n-i] < a[n-i+1]:
            a[n-i], a[n-i-1] = a[n-i-1], a[n-i]
    pt_cuoi = a[n-1]
    return pt_cuoi 
