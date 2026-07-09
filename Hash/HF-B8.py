def tinh_do_lech(danh_sach_hash, m):
    bang_dem = [0] * m
    for h in danh_sach_hash:
        bang_dem[h % m] += 1
        
    trung_binh = len(danh_sach_hash) / m
    chi_square = 0
    for count in bang_dem:
        chi_square += ((count - trung_binh) ** 2) / trung_binh
    return chi_square

hash1 = [10, 20, 30, 40]
hash2 = [1, 2, 3, 4]
print("Do lech (chi-square) cang nho thi phan bo cang deu.")
print("Hash 1 (te) m=10:", tinh_do_lech(hash1, 10))
print("Hash 2 (tot) m=10:", tinh_do_lech(hash2, 10))
