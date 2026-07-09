#Câu 5 (Ứng dụng Hàng đợi - Queue)
#Cho mảng A = [4, 2, 12, 11, -5, 8, 1, 5, 6] và kích thước cửa sổ trượt k = 3. 
#Thay vì tìm giá trị lớn nhất, hãy mô tả quá trình sử dụng cấu trúc Deque (Hàng đợi hai đầu) để tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt. 
#Trình bày trạng thái của Deque ở 3 bước dịch chuyển đầu tiên và đưa ra mảng kết quả.
from collections import deque
A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
def sliding_win_min(A, k):
    dq = deque()
    res = []
    for i in range(len(A)):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and A[dq[-1]] > A[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(A[dq[0]])
    return res

print(sliding_win_min(A, k))
    
