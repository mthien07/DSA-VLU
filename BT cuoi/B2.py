#Câu 2 (Thuật toán Sắp xếp)
#Cho mảng A = [5, 2, 4, 6, 1, 3]. Hãy tính tổng số lần dịch chuyển (shift) phần tử khi áp dụng thuật toán Insertion Sort để sắp xếp mảng theo thứ tự tăng dần. 
# Đại lượng tính được này có mối liên hệ đặc biệt nào với khái niệm "số nghịch thế" (inversions) của mảng ban đầu?

A = [5, 2, 4, 6, 1, 3]
def insertion_sort(a):
    arr = a.copy()
    total_shifts = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j-=1
            shifts += 1
        arr[j + 1] = key
        total_shifts += shifts
    return arr, total_shifts
