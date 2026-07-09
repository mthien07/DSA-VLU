def ham_bam_chuoi_tong(chuoi, m):
    tong = 0
    for ky_tu in chuoi:
        tong += ord(ky_tu)
    return tong % m

m = 10
print("Hash cua 'abc':", ham_bam_chuoi_tong('abc', m))
print("Hash cua 'cba':", ham_bam_chuoi_tong('cba', m))
print("=> Nhuoc diem: Cac dao chu se co cung gia tri hash.")
