def rabin_karp(mau, van_ban):
    p = 31
    m = 10**9 + 9
    len_mau = len(mau)
    len_vb = len(van_ban)
    if len_mau > len_vb: return -1
    
    hash_mau = 0
    hash_cua_so = 0
    p_pow = 1
    
    for i in range(len_mau):
        hash_mau = (hash_mau * p + ord(mau[i])) % m
        hash_cua_so = (hash_cua_so * p + ord(van_ban[i])) % m
        if i < len_mau - 1:
            p_pow = (p_pow * p) % m
            
    for i in range(len_vb - len_mau + 1):
        if hash_mau == hash_cua_so:
            if van_ban[i:i+len_mau] == mau:
                return i
        if i < len_vb - len_mau:
            hash_cua_so = (hash_cua_so - ord(van_ban[i]) * p_pow) % m
            hash_cua_so = (hash_cua_so * p + ord(van_ban[i + len_mau])) % m
            hash_cua_so = (hash_cua_so + m) % m
    return -1

print("Vi tri cua 'abc' trong 'zabcd':", rabin_karp('abc', 'zabcd'))
