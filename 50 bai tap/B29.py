from collections import deque

def max_cua_so_truot(mang, k):
    n = len(mang)
    ket_qua = []
    hang_doi = deque()
    
    for i in range(n):
        if hang_doi and hang_doi[0] < i - k + 1:
            hang_doi.popleft()
            
        while hang_doi and mang[hang_doi[-1]] < mang[i]:
            hang_doi.pop()
            
        hang_doi.append(i)
        
        if i >= k - 1:
            ket_qua.append(mang[hang_doi[0]])
            
    return ket_qua

mang = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_cua_so_truot(mang, k))
