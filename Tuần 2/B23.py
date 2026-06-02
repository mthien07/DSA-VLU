def phan_tu_nho_thu_k_ma_tran(ma_tran: list[list[int]], k: int) -> int:
    n = len(ma_tran)
    def dem_so_luong_nho_hon_hoac_bang(gia_tri_giua: int) -> int:
        so_luong = 0
        hang = n - 1
        cot = 0
        while hang >= 0 and cot < n:
            if ma_tran[hang][cot] <= gia_tri_giua:
                so_luong += (hang + 1)
                cot += 1
            else:
                hang -= 1
        return so_luong

    dau = ma_tran[0][0]
    cuoi = ma_tran[n - 1][n - 1]
    ket_qua = dau
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if dem_so_luong_nho_hon_hoac_bang(giua) >= k:
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua
