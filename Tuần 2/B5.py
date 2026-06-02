def vi_tri_dau_tien(a: list[int], x: int) -> int:
    dau, cuoi = 0, len(a) - 1
    ket_qua = -1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            ket_qua = giua
            cuoi = giua - 1
        elif a[giua] < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return ket_qua

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

def dem_so_lan_xuat_hien(a: list[int], x: int) -> int:
    dau_tien = vi_tri_dau_tien(a, x)
    if dau_tien == -1:
        return 0
    cuoi_cung = vi_tri_cuoi_cung(a, x)
    return cuoi_cung - dau_tien + 1