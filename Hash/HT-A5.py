def nhom_theo_chu_cai_dau(danh_sach_tu):
    bang_nhom = {}
    for tu in danh_sach_tu:
        chu_cai_dau = tu[0]
        if chu_cai_dau not in bang_nhom:
            bang_nhom[chu_cai_dau] = []
        bang_nhom[chu_cai_dau].append(tu)
    return bang_nhom

tu_vung = ["apple", "banana", "apricot", "cherry", "blueberry"]
print("Nhom tu vung:")
print(nhom_theo_chu_cai_dau(tu_vung))
