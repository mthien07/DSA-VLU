import random

def min_hash(tap_hop, num_hashes=5):
    hashes = []
    for _ in range(num_hashes):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        
        min_h = float('inf')
        for x in tap_hop:
            h = (a * hash(x) + b) % 1000
            min_h = min(min_h, h)
        hashes.append(min_h)
    return hashes

tapA = {1, 2, 3, 4}
tapB = {3, 4, 5, 6}
print("MinHash tap A:", min_hash(tapA))
print("MinHash tap B:", min_hash(tapB))
print("Dung ty le trung khop cua cac min-hash de uoc luong do tuong dong Jaccard.")
