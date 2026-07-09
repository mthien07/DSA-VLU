def dien_tich_lon_nhat(h):
    h.append(0)
    ngan_xep = []
    max_area = 0
    
    for i in range(len(h)):
        while ngan_xep and h[ngan_xep[-1]] > h[i]:
            chieu_cao = h[ngan_xep.pop()]
            chieu_rong = i if not ngan_xep else i - ngan_xep[-1] - 1
            max_area = max(max_area, chieu_cao * chieu_rong)
        ngan_xep.append(i)
        
    return max_area

h = [2, 1, 5, 6, 2, 3]
print(dien_tich_lon_nhat(h))
