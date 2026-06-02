def chia_sach(p: list[int], m: int) -> int:
    n = len(p)
    if m > n:
        return -1
    def co_the_phan_chia(so_trang_max: int) -> bool:
        so_hoc_sinh = 1
        so_trang_hien_tai = 0
        for trang in p:
            if so_trang_hien_tai + trang > so_trang_max:
                so_hoc_sinh += 1
                so_trang_hien_tai = trang
                if so_hoc_sinh > m:
                    return False
            else:
                so_trang_hien_tai += trang
        return True

    dau = max(p)
    cuoi = sum(p)
    ket_qua = cuoi
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if co_the_phan_chia(giua):
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua
