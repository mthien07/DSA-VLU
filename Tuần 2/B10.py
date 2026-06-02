def tim_mang_xoay(a: list[int], x: int) -> int:
    dau, cuoi = 0, len(a) - 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            return giua
        if a[dau] <= a[giua]:
            if a[dau] <= x < a[giua]:
                cuoi = giua - 1
            else:
                dau = giua + 1
        else:
            if a[giua] < x <= a[cuoi]:
                dau = giua + 1
            else:
                cuoi = giua - 1
    return -1