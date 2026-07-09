import heapq

def dijkstra_co_ban(do_thi, n, nguon):
    khoang_cach = [float('inf')] * n
    khoang_cach[nguon] = 0
    
    hang_doi = [(0, nguon)]
    
    while hang_doi:
        kc_hien_tai, u = heapq.heappop(hang_doi)
        
        if kc_hien_tai > khoang_cach[u]:
            continue
            
        for v, trong_so in do_thi[u]:
            kc_moi = kc_hien_tai + trong_so
            if kc_moi < khoang_cach[v]:
                khoang_cach[v] = kc_moi
                heapq.heappush(hang_doi, (kc_moi, v))
                
    return khoang_cach

n = 4
do_thi = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 5)],
    2: [(3, 1)],
    3: []
}
print(dijkstra_co_ban(do_thi, n, 0))
