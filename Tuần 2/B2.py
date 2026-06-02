def kiem_tra_ton_tai(a: list[int], x: int) -> bool:
    dau, cuoi = 0, len(a) - 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            return True
        elif a[giua] < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return False
