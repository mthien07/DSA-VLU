def tron_mang(mang1, mang2):
    kq = []
    i = 0
    j = 0
    while i < len(mang1) and j < len(mang2):
        if mang1[i] < mang2[j]:
            kq.append(mang1[i])
            i += 1
        else:
            kq.append(mang2[j])
            j += 1
            
    while i < len(mang1):
        kq.append(mang1[i])
        i += 1
    while j < len(mang2):
        kq.append(mang2[j])
        j += 1
        
    return kq

mang1 = [1, 3, 5]
mang2 = [2, 4]
print(f"Tron {mang1} va {mang2} ->", tron_mang(mang1, mang2))
