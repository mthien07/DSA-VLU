def tim_mang_xoay(mang, x):
    trai = 0
    phai = len(mang) - 1
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua
            
        if mang[trai] <= mang[giua]:
            if mang[trai] <= x < mang[giua]:
                phai = giua - 1
            else:
                trai = giua + 1
        else:
            if mang[giua] < x <= mang[phai]:
                trai = giua + 1
            else:
                phai = giua - 1
                
    return -1

a = [4, 5, 6, 7, 0, 1, 2]
x = 0
print(tim_mang_xoay(a, x))
