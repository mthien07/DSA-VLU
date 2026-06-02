def tim_trong_ma_tran(ma_tran: list[list[int]], x: int) -> bool:
    if not ma_tran or not ma_tran[0]:
        return False
    m, n = len(ma_tran), len(ma_tran[0])
    dau, cuoi = 0, m * n - 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        hang, cot = giua // n, giua % n
        gia_tri = ma_tran[hang][cot]
        if gia_tri == x:
            return True
        elif gia_tri < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return False