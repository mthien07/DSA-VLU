def bam_da_thuc(chuoi, p=31, m=10**9 + 9):
    gia_tri_bam = 0
    p_mu_i = 1
    
    for ky_tu in chuoi:
        gia_tri_bam = (gia_tri_bam + (ord(ky_tu) - ord('a') + 1) * p_mu_i) % m
        p_mu_i = (p_mu_i * p) % m
        
    return gia_tri_bam

chuoi1 = "abc"
chuoi2 = "bca"

ma1 = bam_da_thuc(chuoi1)
ma2 = bam_da_thuc(chuoi2)

print(f"Ma bam cua '{chuoi1}': {ma1}")
print(f"Ma bam cua '{chuoi2}': {ma2}")
print("Giai quyet duoc xung dot do thu tu ky tu thay doi se lam thay doi luy thua cua p.")
