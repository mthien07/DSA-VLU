import heapq

def dijkstra_heap(n, canh, s):
    do_thi = [[] for _ in range(n)]
    for u, v, w in canh:
        do_thi[u].append((v, w))
        
    khoang_cach = [float('inf')] * n
    khoang_cach[s] = 0
    hang_doi = [(0, s)]
    
    while hang_doi:
        d, u = heapq.heappop(hang_doi)
        
        if d > khoang_cach[u]:
            continue
            
        for v, w in do_thi[u]:
            if khoang_cach[u] + w < khoang_cach[v]:
                khoang_cach[v] = khoang_cach[u] + w
                heapq.heappush(hang_doi, (khoang_cach[v], v))
                
    return khoang_cach

canh = [
    (0, 1, 4), (0, 2, 1),
    (2, 1, 2), (1, 3, 1),
    (2, 3, 5)
]
print(dijkstra_heap(4, canh, 0))
