def sap_xep_chon_minh_hoa():
    
    a = [(2, 'A'), (2, 'B'), (1, 'C')]
    print("Truoc khi sap xep:", a)
    n = len(a)
    for i in range(n - 1):
        vi_tri_min = i
        for j in range(i + 1, n):
            if a[j][0] < a[vi_tri_min][0]:
                vi_tri_min = j
        if vi_tri_min != i:
            a[i], a[vi_tri_min] = a[vi_tri_min], a[i]
            
    print("Sau khi sap xep (Selection Sort):", a)
    print("selection sort khong on dinh")

sap_xep_chon_minh_hoa()
