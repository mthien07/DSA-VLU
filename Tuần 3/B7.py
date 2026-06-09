def bubble_sort_char(arr):
    n = len(arr)
    if n <= 1:
        return arr
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr