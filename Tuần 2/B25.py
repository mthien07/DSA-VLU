def luc_tu_nam_cham(x: list[int], m: int) -> int:
    x_sap_xep = sorted(x)
    def co_the_dat_nam_cham(luc_tu_min: int) -> bool:
        so_nam_cham_da_dat = 1
        vi_tri_cuoi = x_sap_xep[0]
        for i in range(1, len(x_sap_xep)):
            if x_sap_xep[i] - vi_tri_cuoi >= luc_tu_min:
                so_nam_cham_da_dat += 1
                vi_tri_cuoi = x_sap_xep[i]
                if so_nam_cham_da_dat >= m:
                    return True
        return False

    dau = 1
    cuoi = x_sap_xep[-1] - x_sap_xep[0]
    ket_qua = 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if co_the_dat_nam_cham(giua):
            ket_qua = giua
            dau = giua + 1
        else:
            cuoi = giua - 1
    return ket_qua
