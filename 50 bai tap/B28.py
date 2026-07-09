from collections import deque

def sinh_so_nhi_phan(n):
    if n <= 0:
        return []
        
    ket_qua = []
    hang_doi = deque(['1'])
    
    for _ in range(n):
        so_hien_tai = hang_doi.popleft()
        ket_qua.append(so_hien_tai)
        
        hang_doi.append(so_hien_tai + '0')
        hang_doi.append(so_hien_tai + '1')
        
    return ket_qua

print(sinh_so_nhi_phan(5))
