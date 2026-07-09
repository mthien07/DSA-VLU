def xoa_trung_lap(mang):
    da_thay = set()
    kq = []
    for so in mang:
        if so not in da_thay:
            da_thay.add(so)
            kq.append(so)
    return kq

mang = [3, 1, 3, 2, 1]
print(f"Truoc: {mang} -> Sau: {xoa_trung_lap(mang)}")
