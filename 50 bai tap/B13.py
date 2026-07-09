def tron_va_dem(mang, tam, trai, giua, phai):
    i = trai
    j = giua + 1
    k = trai
    dem_nghich_the = 0
    
    while i <= giua and j <= phai:
        if mang[i] <= mang[j]:
            tam[k] = mang[i]
            i += 1
        else:
            tam[k] = mang[j]
            dem_nghich_the += (giua - i + 1)
            j += 1
        k += 1
        
    while i <= giua:
        tam[k] = mang[i]
        i += 1
        k += 1
        
    while j <= phai:
        tam[k] = mang[j]
        j += 1
        k += 1
        
    for x in range(trai, phai + 1):
        mang[x] = tam[x]
        
    return dem_nghich_the

def merge_sort_dem(mang, tam, trai, phai):
    dem_nghich_the = 0
    if trai < phai:
        giua = (trai + phai) // 2
        dem_nghich_the += merge_sort_dem(mang, tam, trai, giua)
        dem_nghich_the += merge_sort_dem(mang, tam, giua + 1, phai)
        dem_nghich_the += tron_va_dem(mang, tam, trai, giua, phai)
    return dem_nghich_the

a = [2, 4, 1, 3, 5]
n = len(a)
tam = [0] * n
so_nghich_the = merge_sort_dem(a, tam, 0, n - 1)
print(f"So nghich the: {so_nghich_the}")
