def rabin_karp(van_ban, mau):
    n = len(van_ban)
    m = len(mau)
    p = 31
    mod = 10**9 + 9
    
    if m > n or m == 0:
        return []
        
    p_mu_m_tru_1 = 1
    for _ in range(m - 1):
        p_mu_m_tru_1 = (p_mu_m_tru_1 * p) % mod
        
    bam_mau = 0
    bam_cua_so = 0
    
    for i in range(m):
        bam_mau = (bam_mau * p + ord(mau[i])) % mod
        bam_cua_so = (bam_cua_so * p + ord(van_ban[i])) % mod
        
    ket_qua = []
    
    for i in range(n - m + 1):
        if bam_mau == bam_cua_so:
            if van_ban[i:i+m] == mau:
                ket_qua.append(i)
                
        if i < n - m:
            bam_cua_so = (bam_cua_so - ord(van_ban[i]) * p_mu_m_tru_1) % mod
            bam_cua_so = (bam_cua_so * p + ord(van_ban[i + m])) % mod
            bam_cua_so = (bam_cua_so + mod) % mod
            
    return ket_qua

van_ban = "xabc"
mau = "abc"
print(f"Tim '{mau}' trong '{van_ban}' tai cac vi tri: {rabin_karp(van_ban, mau)}")
