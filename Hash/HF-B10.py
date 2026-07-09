import math

def multiplication_hash(k, m):
    A = (math.sqrt(5) - 1) / 2
    phan_thap_phan = (k * A) % 1
    return math.floor(m * phan_thap_phan)

print("k=123, m=10 ->", multiplication_hash(123, 10))
