def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
print("Mảng chưa được sắp xếp là: ", arr)
bubble_sort_descending(arr)
print("Mảng sau khi sắp xếp từ lớn đến bé là:", arr)