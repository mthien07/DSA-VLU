def chen_x_insert_sort(a, x):
    a.append(x)
    j = len(a) - 2
    while j >= 0 and a[j] > x:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = x
    return a
