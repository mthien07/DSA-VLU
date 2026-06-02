def phan_tu_thu_k_bi_thieu(a: list[int], k: int) -> int:
    dau, cuoi = 0, len(a) - 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        so_bi_thieu = a[giua] - (giua + 1)
        if so_bi_thieu < k:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return k + dau
