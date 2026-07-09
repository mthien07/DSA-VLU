def tron_khoang(khoang_list):
    if len(khoang_list) == 0: return []
    
    khoang_list.sort()
    
    kq = [khoang_list[0]]
    for i in range(1, len(khoang_list)):
        khoang_hien_tai = khoang_list[i]
        khoang_cuoi_kq = kq[-1]
        
        if khoang_hien_tai[0] <= khoang_cuoi_kq[1]:
            kq[-1][1] = max(khoang_cuoi_kq[1], khoang_hien_tai[1])
        else:
            kq.append(khoang_hien_tai)
            
    return kq

cac_khoang = [[1, 3], [2, 6], [8, 10]]
print("Truoc:", cac_khoang)
print("Sau khi tron:", tron_khoang(cac_khoang))
