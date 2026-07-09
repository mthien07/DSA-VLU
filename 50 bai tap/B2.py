def tim_vi_tri_dau(mang, x):
    trai = 0
    phai = len(mang) - 1
    ket_qua = -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            ket_qua = giua
            phai = giua - 1
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

def tim_vi_tri_cuoi(mang, x):
    trai = 0
    phai = len(mang) - 1
    ket_qua = -1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            ket_qua = giua
            trai = giua + 1
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return ket_qua

def dem_so_lan_xuat_hien(mang, x):
    dau = tim_vi_tri_dau(mang, x)
    if dau == -1:
        return -1, -1, 0
    cuoi = tim_vi_tri_cuoi(mang, x)
    dem = cuoi - dau + 1
    return dau, cuoi, dem

a = [1, 2, 2, 2, 3]
x = 2
dau, cuoi, dem = dem_so_lan_xuat_hien(a, x)
print(f"dau={dau}, cuoi={cuoi}, dem={dem}")
