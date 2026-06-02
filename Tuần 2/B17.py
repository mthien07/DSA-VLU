def suc_chua_tau_hang(trong_luong: list[int], so_ngay: int) -> int:
    def co_the_van_chuyen(suc_chua: int) -> bool:
        trong_luong_hien_tai = 0
        so_ngay_can_thiet = 1
        for nang in trong_luong:
            if trong_luong_hien_tai + nang > suc_chua:
                so_ngay_can_thiet += 1
                trong_luong_hien_tai = nang
                if so_ngay_can_thiet > so_ngay:
                    return False
            else:
                trong_luong_hien_tai += nang
        return so_ngay_can_thiet <= so_ngay

    dau = max(trong_luong)
    cuoi = sum(trong_luong)
    ket_qua = cuoi
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if co_the_van_chuyen(giua):
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua
