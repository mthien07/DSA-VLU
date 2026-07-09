def phan_tu_nhieu_nhat(mang):
    tan_suat = {}
    max_tan_suat = 0
    ket_qua = None
    
    for phan_tu in mang:
        tan_suat[phan_tu] = tan_suat.get(phan_tu, 0) + 1
        if tan_suat[phan_tu] > max_tan_suat:
            max_tan_suat = tan_suat[phan_tu]
            ket_qua = phan_tu
            
    return ket_qua

mang = [1, 2, 2, 3, 2]
print(phan_tu_nhieu_nhat(mang))
