import heapq

def partial_selection_k(arr, k):
    a = arr.copy()
    n = len(a)
    for i in range (k):
        min_idx = i
        for j in range (i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a[:k]

def heap_k_smallest(arr, k):
    return heapq.nsmallest(k, arr)
