def bam_ascii_don_gian(chuoi, m):
    tong = 0
    for ky_tu in chuoi:
        tong += ord(ky_tu)
    return tong % m

chuoi1 = "abc"
chuoi2 = "bca"
m = 100

ma1 = bam_ascii_don_gian(chuoi1, m)
ma2 = bam_ascii_don_gian(chuoi2, m)

print(f"Ma bam cua '{chuoi1}': {ma1}")
print(f"Ma bam cua '{chuoi2}': {ma2}")
print("Diem yeu: Dao lon ky tu (anagrams) se tao ra cung ma bam (xung dot).")
