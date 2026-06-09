def bubble_sort_count_comp(arr):
    n = len(arr)
    count = 0
    if n <= 1:
        return arr, count 
    for i in range (n-1):
        for j in range (0, n-i-1):
            count += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, count 