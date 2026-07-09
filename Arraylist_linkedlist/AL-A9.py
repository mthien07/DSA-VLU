def dao_nguoc_tai_cho(mang):
    trai = 0
    phai = len(mang) - 1
    while trai < phai:
        tam = mang[trai]
        mang[trai] = mang[phai]
        mang[phai] = tam
        trai += 1
        phai -= 1
    return mang

mang = [1, 2, 3, 4]
print("Truoc:", mang)
print("Sau:", dao_nguoc_tai_cho(mang))
