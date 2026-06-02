def vi_tri_cuoi_cung(a: list[int], x: int) -> int:
    dau, cuoi = 0, len(a) - 1
    ket_qua = -1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            ket_qua = giua
            dau = giua + 1
        elif a[giua] < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return ket_qua