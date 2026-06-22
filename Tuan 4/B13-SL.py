def selection_sort_students(students):
    a = students.copy()
    n = len(a)
    for i in range (n - 1):
        min_idx = i
        for j in range (i + 1, n):
            if a[j][1] < a[min_idx][1]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
