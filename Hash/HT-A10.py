def chu_cai_khong_lap_dau_tien(chuoi):
    bang_dem = {}
    for ky_tu in chuoi:
        if ky_tu in bang_dem:
            bang_dem[ky_tu] += 1
        else:
            bang_dem[ky_tu] = 1
            
    for ky_tu in chuoi:
        if bang_dem[ky_tu] == 1:
            return ky_tu
    return None

chuoi = 'leetcode'
print(f"Chu cai dau tien khong lap trong '{chuoi}' la:", chu_cai_khong_lap_dau_tien(chuoi))
