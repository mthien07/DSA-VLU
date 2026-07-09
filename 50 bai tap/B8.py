def sap_xep_noi_bot_toi_uu(mang):
    n = len(mang)
    so_luot = 0
    for i in range(n):
        da_swap = False
        so_luot += 1
        for j in range(0, n - i - 1):
            if mang[j] > mang[j + 1]:
                mang[j], mang[j + 1] = mang[j + 1], mang[j]
                da_swap = True
        if not da_swap:
            break
    return so_luot

a = [1, 2, 3, 4]
so_luot = sap_xep_noi_bot_toi_uu(a)
print(f"{so_luot} luot roi dung")
