def koko_an_chuoi(cac_dong: list[int], h: int) -> int:
    def co_the_an_het(toc_do: int) -> bool:
        so_gio = 0
        for dong in cac_dong:
            so_gio += (dong + toc_do - 1) // toc_do
            if so_gio > h:
                return False
        return so_gio <= h

    dau = 1
    cuoi = max(cac_dong)
    ket_qua = cuoi
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if co_the_an_het(giua):
            ket_qua = giua
            cuoi = giua - 1
        else:
            dau = giua + 1
    return ket_qua
