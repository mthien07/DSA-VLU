def selection_sort_print_steps(arr):
    a = arr.copy()
    n = len(a)
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Buoc {i+1}: {a}")
