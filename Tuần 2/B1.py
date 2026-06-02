def tim_kiem_co_ban(a: list[int], x: int) -> int:
    dau, cuoi = 0, len(a) - 1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            return giua
        elif a[giua] < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
    return -1