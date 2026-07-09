def tim_kiem_nhi_phan_vi_tri(mang, phai, x):
    trai = 0
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua + 1
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
    return trai

def sap_xep_chen_nhi_phan(mang):
    n = len(mang)
    so_shift = 0
    for i in range(1, n):
        khoa = mang[i]
        j = i - 1
        vi_tri = tim_kiem_nhi_phan_vi_tri(mang, j, khoa)
        
        while j >= vi_tri:
            mang[j + 1] = mang[j]
            so_shift += 1
            j -= 1
        mang[j + 1] = khoa
    return so_shift

a = [3, 2, 1]
sap_xep_chen_nhi_phan(a)
print("giam so sanh, shift giu nguyen")
