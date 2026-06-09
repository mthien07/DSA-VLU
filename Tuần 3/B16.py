def swap_bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    so_lan_swap = 0
    for i in range (n -1):
        swapped = False
        for j in range (0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                so_lan_swap += 1
                swapped = True
        if not swapped:
            break
    return a, so_lan_swap

def bubble_sort_count_inversion(a):
    n = len(a)
    so_nghich_the = 0
    for i in range (n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                so_nghich_the += 1
    return so_nghich_the 

 #thuat toan bubblesort hoat dong theo cach duyet qua mang va hoan doi cac phan tu ngay canh nhau
 #tac dong cua swap: khi phat hien a[j] > a[j+1] thi hoan doi, khi ta hoan doi thi nghich the giua chung triet tieu di 1(giam di 1)
 #vi bubblesort chi hoan doi 2 phan tu ke ben, nen vi tri tuong doi 2 ptu nay so voi cac ptu trong mang khong bi thay doi. Do do tong so lan hoan doi bat buoc bang chinh xac so nghich the ban dau