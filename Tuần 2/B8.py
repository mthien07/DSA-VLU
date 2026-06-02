def can_bac_hai_nguyen(n: int) -> int:
    if n < 2:
        return n
    dau, cuoi = 1, n
    ket_qua = 0
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if giua * giua == n:
            return giua
        elif giua * giua < n:
            ket_qua = giua
            dau = giua + 1
        else:
            cuoi = giua - 1
    return ket_qua
