def phan_tu_don_le(a: list[int]) -> int:
    dau, cuoi = 0, len(a) - 1
    while dau < cuoi:
        giua = (dau + cuoi) // 2
        if giua % 2 == 1:
            giua -= 1
        if a[giua] == a[giua + 1]:
            dau = giua + 2
        else:
            cuoi = giua
    return a[dau]