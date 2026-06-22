def online_insertion_sort(stream):
    """Sap xep truc tuyen: moi phan tu den, chen vao mang da sap xep"""
    a = []
    for x in stream:
        # Chen x vao dung vi tri trong mang da sap xep
        a.append(x)
        j = len(a) - 2
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x
        print(a.copy())
