import random

class UniversalHash:
    def __init__(self, m, p=10**9+7):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

uh = UniversalHash(10)
print("a:", uh.a, "b:", uh.b)
print("Hash cua 123:", uh.hash(123))
print("Chong duoc ke xau co y dua vao du lieu gay va cham vi a,b la ngau nhien!")
