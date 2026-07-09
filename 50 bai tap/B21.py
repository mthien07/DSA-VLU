def kiem_tra_ngoac(chuoi):
    ngan_xep = []
    cap_ngoac = {')': '(', ']': '[', '}': '{'}
    
    for ky_tu in chuoi:
        if ky_tu in '([{':
            ngan_xep.append(ky_tu)
        elif ky_tu in ')]}':
            if not ngan_xep or ngan_xep[-1] != cap_ngoac[ky_tu]:
                return False
            ngan_xep.pop()
            
    return len(ngan_xep) == 0

print(kiem_tra_ngoac('([]{})'))
print(kiem_tra_ngoac('([)]'))
