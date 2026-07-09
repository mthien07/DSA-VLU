def next_greater_element(mang):
    n = len(mang)
    ket_qua = [-1] * n
    ngan_xep = []
    
    for i in range(n):
        while ngan_xep and mang[ngan_xep[-1]] < mang[i]:
            idx = ngan_xep.pop()
            ket_qua[idx] = mang[i]
        ngan_xep.append(i)
        
    return ket_qua

mang = [2, 1, 3]
print(next_greater_element(mang))
