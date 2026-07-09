def dem_tan_suat(mang):
    bang_dem = {}
    for phan_tu in mang:
        if phan_tu in bang_dem:
            bang_dem[phan_tu] += 1
        else:
            bang_dem[phan_tu] = 1
    return bang_dem

mang = ['a', 'b', 'a', 'c', 'a']
print(f"Tan suat cua {mang}:")
print(dem_tan_suat(mang))
