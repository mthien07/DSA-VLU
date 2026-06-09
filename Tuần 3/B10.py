def bubble_sort_ee_count(a):
    n = len(a)
    count = 0
    if n<=1:
        return a, count
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                count += 1
        if not swapped:
            break
    return a, count 