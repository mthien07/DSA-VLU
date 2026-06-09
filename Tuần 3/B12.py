def bubble_sort_length(str_arr):
    n = len(str_arr)
    if n <= 1:
        return str_arr
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if len(str_arr[j]) > len(str_arr[j+1]):
                str_arr[j], str_arr[j+1] = str_arr[j+1], str_arr[j]
                swapped = True
        if not swapped:
            break
    return str_arr