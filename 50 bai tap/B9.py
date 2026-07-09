def sap_xep_chen(mang):
    n = len(mang)
    so_shift = 0
    for i in range(1, n):
        khoa = mang[i]
        j = i - 1
        while j >= 0 and khoa < mang[j]:
            mang[j + 1] = mang[j]
            so_shift += 1
            j -= 1
        mang[j + 1] = khoa
    return so_shift

a = [3, 2, 1]
so_shift = sap_xep_chen(a)
print(f"{so_shift} shift")
