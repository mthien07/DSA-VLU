import heapq

def dijkstra_truy_vet(do_thi, n, nguon, dich):
    khoang_cach = [float('inf')] * n
    cha = [-1] * n
    khoang_cach[nguon] = 0
    
    hang_doi = [(0, nguon)]
    
    while hang_doi:
        kc_hien_tai, u = heapq.heappop(hang_doi)
        
        if u == dich:
            break
            
        if kc_hien_tai > khoang_cach[u]:
            continue
            
        for v, trong_so in do_thi[u]:
            kc_moi = kc_hien_tai + trong_so
            if kc_moi < khoang_cach[v]:
                khoang_cach[v] = kc_moi
                cha[v] = u
                heapq.heappush(hang_doi, (kc_moi, v))
                
    duong_di = []
    hien_tai = dich
    while hien_tai != -1:
        duong_di.append(hien_tai)
        hien_tai = cha[hien_tai]
        
    duong_di.reverse()
    if duong_di[0] == nguon:
        return duong_di
    return []

do_thi = {
    0: [(2, 2), (1, 5)],
    1: [(3, 1)],
    2: [(1, 1), (3, 4)],
    3: [(4, 2)],
    4: []
}
duong_di = dijkstra_truy_vet(do_thi, 5, 0, 4)
print(" -> ".join(map(str, duong_di)))
