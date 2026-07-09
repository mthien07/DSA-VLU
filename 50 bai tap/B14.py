def sap_xep_shell(mang, day_gap):
    n = len(mang)
    tong_shift = 0
    
    for gap in day_gap:
        for i in range(gap, n):
            khoa = mang[i]
            j = i
            while j >= gap and mang[j - gap] > khoa:
                mang[j] = mang[j - gap]
                tong_shift += 1
                j -= gap
            mang[j] = khoa
            
    return tong_shift

a = [9, 8, 3, 7, 5, 6, 4, 1]
day_gap = [4, 2, 1]
so_shift = sap_xep_shell(a, day_gap)
print(f"Tong so shift: {so_shift}")
