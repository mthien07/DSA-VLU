def k_phan_tu_gan_nhat(a: list[int], k: int, x: int) -> list[int]:
    dau, cuoi = 0, len(a) - k
    while dau < cuoi:
        giua = (dau + cuoi) // 2
        if x - a[giua] > a[giua + k] - x:
            dau = giua + 1
        else:
            cuoi = giua
    return a[dau:dau + k]
