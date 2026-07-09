def dem_mang_con_tong_k(mang, k):
    tong_cong_don = 0
    dem = 0
    bang_bam = {0: 1}
    
    for so in mang:
        tong_cong_don += so
        if tong_cong_don - k in bang_bam:
            dem += bang_bam[tong_cong_don - k]
            
        bang_bam[tong_cong_don] = bang_bam.get(tong_cong_don, 0) + 1
        
    return dem

mang = [1, 1, 1]
k = 2
print(dem_mang_con_tong_k(mang, k))
