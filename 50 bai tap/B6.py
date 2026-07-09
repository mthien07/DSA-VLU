def kiem_tra_chia(mang, k, tong_toi_da):
    so_doan = 1
    tong_hien_tai = 0
    for so in mang:
        if tong_hien_tai + so > tong_toi_da:
            so_doan += 1
            tong_hien_tai = so
            if so_doan > k:
                return False
        else:
            tong_hien_tai += so
    return True

def chia_mang(mang, k):
    trai = max(mang)
    phai = sum(mang)
    ket_qua = phai
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if kiem_tra_chia(mang, k, giua):
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
            
    return ket_qua

a = [7, 2, 5, 10, 8]
k = 2
print(chia_mang(a, k))
