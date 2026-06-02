def chia_mang_tong_lon_nhat_nho_nhat(a: list[int], k: int) -> int:
    def co_the_chia_mang(tong_max: int) -> bool:
        so_doan = 1
        tong_hien_tai = 0
        for so in a:
            if tong_hien_tai + so > tong_max:
                so_doan += 1
                tong_hien_tai = so
                if so_doan > k:
                    return False
            else:
                tong_hien_tai += so
        return True

    dau = max(a)
    cuoi = sum(a)
    ket_qua = cuoi
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if co_the_chia_mang(giua):
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua
