def dao_nguoc(mang, trai, phai):
    while trai < phai:
        mang[trai], mang[phai] = mang[phai], mang[trai]
        trai += 1
        phai -= 1

def xoay_mang(mang, k):
    n = len(mang)
    if n == 0: return mang
    k = k % n
    
    dao_nguoc(mang, 0, n - 1)
    dao_nguoc(mang, 0, k - 1)
    dao_nguoc(mang, k, n - 1)
    
    return mang

mang = [1, 2, 3, 4, 5]
k = 2
print(f"Xoay mang {mang} k={k} ->", xoay_mang(mang.copy(), k))
