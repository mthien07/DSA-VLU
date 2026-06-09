def bubble_sort_singly_linked_list(l):
    n = len(l)
    if n <= 1:
        return l
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if not swapped:
            break
    return l