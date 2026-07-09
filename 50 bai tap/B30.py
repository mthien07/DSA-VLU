from collections import deque

def thoi_gian_cam_thoi(luoi):
    hang = len(luoi)
    cot = len(luoi[0])
    
    hang_doi = deque()
    cam_tuoi = 0
    
    for r in range(hang):
        for c in range(cot):
            if luoi[r][c] == 2:
                hang_doi.append((r, c))
            elif luoi[r][c] == 1:
                cam_tuoi += 1
                
    if cam_tuoi == 0:
        return 0
        
    thoi_gian = 0
    huong = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while hang_doi and cam_tuoi > 0:
        thoi_gian += 1
        so_luong_cap_nhat = len(hang_doi)
        
        for _ in range(so_luong_cap_nhat):
            r, c = hang_doi.popleft()
            
            for dr, dc in huong:
                nr, nc = r + dr, c + dc
                if 0 <= nr < hang and 0 <= nc < cot and luoi[nr][nc] == 1:
                    luoi[nr][nc] = 2
                    cam_tuoi -= 1
                    hang_doi.append((nr, nc))
                    
    return thoi_gian if cam_tuoi == 0 else -1

luoi = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
print(f"{thoi_gian_cam_thoi(luoi)} phut")
