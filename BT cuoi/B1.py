#Câu 1 (Chia mảng - Ứng dụng Tìm kiếm Nhị phân)
#Một công ty vận tải cần giao các kiện hàng có khối lượng lần lượt là W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
# Công ty chỉ có K = 5 xe tải, và mỗi xe chỉ được chở các kiện hàng xếp liên tiếp nhau trong danh sách. 
# Hãy dùng thuật toán tìm kiếm nhị phân để xác định tải trọng tối thiểu của một chiếc xe sao cho có thể chở hết tất cả kiện hàng trong một lượt. 
# Giải thích cách chia kiện hàng cho 5 xe với tải trọng tìm được.

W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 5
def min_capacity(W, K):
    def co_the_tai(capacity):
        trucks = 1
        current_load = 0
        for weight in W:
            if current_load + weight > capacity:
                trucks += 1
                current_load = weight
            else:
                current_load += weight
            return trucks <= K
    low = max(W)
    high = sum(W)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if co_the_tai(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(min_capacity(W,K)) 
