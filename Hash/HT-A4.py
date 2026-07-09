def phan_tu_chung(mang1, mang2):
    tap_hop = set()
    for phan_tu in mang1:
        tap_hop.add(phan_tu)
        
    kq = []
    for phan_tu in mang2:
        if phan_tu in tap_hop:
            kq.append(phan_tu)
            tap_hop.remove(phan_tu)
    return kq

mang1 = [1, 2, 3]
mang2 = [2, 3, 4]
print("Phan tu chung:", phan_tu_chung(mang1, mang2))
