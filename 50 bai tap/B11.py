def sap_xep_chon(mang):
    n = len(mang)
    so_so_sanh = 0
    for i in range(n - 1):
        vi_tri_min = i
        for j in range(i + 1, n):
            so_so_sanh += 1
            if mang[j] < mang[vi_tri_min]:
                vi_tri_min = j
        if vi_tri_min != i:
            mang[i], mang[vi_tri_min] = mang[vi_tri_min], mang[i]
    return so_so_sanh

a = [5, 4, 3, 2, 1]
so_so_sanh = sap_xep_chon(a)
print(f"luon {so_so_sanh} so sanh")
