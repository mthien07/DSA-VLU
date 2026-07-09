def dem_va_cham(danh_sach_khoa, ham_bam_func, m):
    bang_dem = {}
    va_cham = 0
    for khoa in danh_sach_khoa:
        h = ham_bam_func(khoa, m)
        if h in bang_dem:
            bang_dem[h] += 1
            va_cham += 1
        else:
            bang_dem[h] = 1
    return va_cham

def ham_bam_te(k, m):
    return len(str(k)) % m

khoa = ["apple", "banana", "cat", "dog", "elephant"]
print("So va cham:", dem_va_cham(khoa, ham_bam_te, 10))
