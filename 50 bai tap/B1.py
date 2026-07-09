def tim_kiem_nhi_phan(mang, x):
    trai = 0
    phai = len(mang) - 1
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == x:
            return giua
        elif mang[giua] < x:
            trai = giua + 1
        else:
            phai = giua - 1
            
    return -1

a = [1, 3, 5, 7, 9]
x = 7
print(tim_kiem_nhi_phan(a, x))
