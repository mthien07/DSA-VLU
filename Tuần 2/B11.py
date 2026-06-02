def tim_min_mang_xoay(a: list[int]) -> int:
    if not a:
        raise ValueError("Mảng không được rỗng")
    dau, cuoi = 0, len(a) - 1
    if a[dau] <= a[cuoi]:
        return a[dau]
    while dau < cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] > a[cuoi]:
            dau = giua + 1
        else:
            cuoi = giua
    return a[dau]
