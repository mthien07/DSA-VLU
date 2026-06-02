import math

def giam_khoang_cach_tram_xang(x: list[int], k: int) -> float:
    def co_the_dat_tram(d: float) -> bool:
        so_tram_moi = 0
        for i in range(len(x) - 1):
            do_dai_doan = x[i+1] - x[i]
            if do_dai_doan > d:
                so_tram_moi += math.ceil(do_dai_doan / d - 1e-9) - 1
                if so_tram_moi > k:
                    return False
        return so_tram_moi <= k

    dau = 0.0
    cuoi = float(x[-1] - x[0])
    for _ in range(80):
        giua = (dau + cuoi) / 2
        if co_the_dat_tram(giua):
            cuoi = giua
        else:
            dau = giua
    return dau
