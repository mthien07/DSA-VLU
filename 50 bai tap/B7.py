def sap_xep_noi_bot(mang):
    n = len(mang)
    so_swap = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if mang[j] > mang[j + 1]:
                mang[j], mang[j + 1] = mang[j + 1], mang[j]
                so_swap += 1
    return so_swap

a = [2, 3, 1]
so_swap = sap_xep_noi_bot(a)
print(f"{so_swap} swap")
