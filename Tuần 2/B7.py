def tim_upper_bound(a: list[int], x: int) -> int:
    dau, cuoi = 0, len(a) - 1
    ket_qua = len(a)
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] > x:
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua