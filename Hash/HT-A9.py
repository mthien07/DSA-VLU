def two_sum(mang, target):
    bang_bam = {}
    for i in range(len(mang)):
        phan_bu = target - mang[i]
        if phan_bu in bang_bam:
            return (bang_bam[phan_bu], i)
        bang_bam[mang[i]] = i
    return None

mang = [2, 7, 11]
target = 9
print(f"Two sum cua {mang} target {target} ->", two_sum(mang, target))
