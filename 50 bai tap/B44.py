def nhom_anagrams(mang_chuoi):
    nhom = {}
    
    for chuoi in mang_chuoi:
        khoa = "".join(sorted(chuoi))
        if khoa not in nhom:
            nhom[khoa] = []
        nhom[khoa].append(chuoi)
        
    return list(nhom.values())

mang = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(nhom_anagrams(mang))
