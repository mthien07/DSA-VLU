def hai_tong(mang, muc_tieu):
    trai = 0
    phai = len(mang) - 1
    ket_qua = []
    
    while trai < phai:
        tong_hien_tai = mang[trai] + mang[phai]
        if tong_hien_tai == muc_tieu:
            ket_qua.append((mang[trai], mang[phai]))
            trai += 1
            phai -= 1
        elif tong_hien_tai < muc_tieu:
            trai += 1
        else:
            phai -= 1
            
    return ket_qua

mang = [1, 2, 3, 4]
muc_tieu = 5
print(hai_tong(mang, muc_tieu))
