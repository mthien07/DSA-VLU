def so_luot_bubble_sort(ban_dau, hien_tai):
    vtri_ban_dau = {}
    for i in range ( len(ban_dau)):
        vtri_ban_dau[ban_dau[i]] = i
    max = 0
    for j in range (len(hien_tai)):
        phan_tu = hien_tai[j]
        i = vtri_ban_dau[phan_tu]
        if i > j:
            lui = i - j
            if lui > max:
                max = lui
    return max 

dau = [1-4]
sau =[1-4]
print(f"dau = {dau}, sau = {sau} -> {so_luot_bubble_sort(dau, sau)} luot")
