def trung_vi_hai_mang(a: list[int], b: list[int]) -> float:
    A, B = a, b
    m, n = len(A), len(B)
    if m > n:
        A, B = B, A
        m, n = n, m
    dau, cuoi = 0, m
    nua_do_dai = (m + n + 1) // 2
    while dau <= cuoi:
        i = (dau + cuoi) // 2
        j = nua_do_dai - i
        A_trai = A[i - 1] if i > 0 else float('-inf')
        A_phai = A[i] if i < m else float('inf')
        B_trai = B[j - 1] if j > 0 else float('-inf')
        B_phai = B[j] if j < n else float('inf')
        if A_trai <= B_phai and B_trai <= A_phai:
            if (m + n) % 2 == 1:
                return float(max(A_trai, B_trai))
            else:
                return (max(A_trai, B_trai) + min(A_phai, B_phai)) / 2.0
        elif A_trai > B_phai:
            cuoi = i - 1
        else:
            dau = i + 1
    raise ValueError("Mảng đầu vào chưa được sắp xếp hoặc không hợp lệ")
