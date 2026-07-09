def hash_combine(a, b):
    return hash(a) ^ (hash(b) + 0x9e3779b9 + (hash(a) << 6) + (hash(a) >> 2))

a = 5
b = 10
print(f"Hash cua cap ({a}, {b}):", hash_combine(a, b))
print(f"Hash cua cap ({b}, {a}):", hash_combine(b, a))
