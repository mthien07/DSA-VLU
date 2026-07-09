def dem_doan_con_bang_k(mang, k):
    bang_bam = {0: 1}
    tong_hien_tai = 0
    dem = 0
    
    for so in mang:
        tong_hien_tai += so
        if tong_hien_tai - k in bang_bam:
            dem += bang_bam[tong_hien_tai - k]
            
        if tong_hien_tai in bang_bam:
            bang_bam[tong_hien_tai] += 1
        else:
            bang_bam[tong_hien_tai] = 1
            
    return dem

mang = [1, 1, 1]
k = 2
print(f"So doan con cua {mang} bang {k} la:", dem_doan_con_bang_k(mang, k))
