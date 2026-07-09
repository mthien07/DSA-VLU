import heapq

def dijkstra_luoi(luoi):
    hang = len(luoi)
    cot = len(luoi[0])
    
    khoang_cach = [[float('inf')] * cot for _ in range(hang)]
    khoang_cach[0][0] = luoi[0][0]
    
    hang_doi = [(luoi[0][0], 0, 0)]
    huong = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while hang_doi:
        chiphi_ht, r, c = heapq.heappop(hang_doi)
        
        if r == hang - 1 and c == cot - 1:
            return chiphi_ht
            
        if chiphi_ht > khoang_cach[r][c]:
            continue
            
        for dr, dc in huong:
            nr, nc = r + dr, c + dc
            if 0 <= nr < hang and 0 <= nc < cot:
                chiphi_moi = chiphi_ht + luoi[nr][nc]
                if chiphi_moi < khoang_cach[nr][nc]:
                    khoang_cach[nr][nc] = chiphi_moi
                    heapq.heappush(hang_doi, (chiphi_moi, nr, nc))
                    
    return -1

luoi = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(dijkstra_luoi(luoi))
