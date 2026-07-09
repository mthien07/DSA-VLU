def hash_set(tap_hop):
    hash_val = 0
    for phan_tu in tap_hop:
        hash_val ^= hash(phan_tu)
    return hash_val

tap1 = [1, 2, 3]
tap2 = [3, 1, 2]
print("Hash tap 1:", hash_set(tap1))
print("Hash tap 2:", hash_set(tap2))
