#bubblesort chay trong khoang O(n^2) nhung khi co early exit thi se chay trong khoang O(n)
import time
def bubble_sort_early_exit_k(a):
    n = len(a)
    so_luot = 0
    for i in range (n-1):
        so_luot += 1
        swapped = False
        for j in range (0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return so_luot
