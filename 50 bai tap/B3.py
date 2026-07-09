def lower_bound(mang, x):
    trai = 0
    phai = len(mang) - 1
    ket_qua = len(mang)
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] >= x:
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

def upper_bound(mang, x):
    trai = 0
    phai = len(mang) - 1
    ket_qua = len(mang)
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] > x:
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
    return ket_qua

a = [1, 3, 5, 7]
x = 4
idx = lower_bound(a, x)
print(f"lower=idx {idx}")
