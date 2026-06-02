def tim_dinh(a: list[int]) -> int:
    dau, cuoi = 0, len(a) - 1
    while dau < cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] < a[giua + 1]:
            dau = giua + 1
        else:
            cuoi = giua
    return dau