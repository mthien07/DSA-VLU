def remove_if_even(mang):
    ghi = 0
    for doc in range(len(mang)):
        if mang[doc] % 2 != 0:
            mang[ghi] = mang[doc]
            ghi += 1
            
    while len(mang) > ghi:
        mang.pop()
    return mang

mang = [1, 2, 3, 4]
print("Ban dau:", mang)
print("Sau khi xoa chan:", remove_if_even(mang))
