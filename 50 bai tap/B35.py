def kiem_tra_doi_xung(mang):
    trai = 0
    phai = len(mang) - 1
    
    while trai < phai:
        if mang[trai] != mang[phai]:
            return False
        trai += 1
        phai -= 1
        
    return True

print(kiem_tra_doi_xung([1, 2, 2, 1]))
