def polynomial_hash(chuoi, p=31, m=10**9 + 9):
    hash_val = 0
    p_pow = 1
    for ky_tu in chuoi:
        hash_val = (hash_val + ord(ky_tu) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_val

print("Hash cua 'abc':", polynomial_hash('abc'))
print("Hash cua 'cba':", polynomial_hash('cba'))
print("=> Da khac phuc duoc loi dao chu!")
