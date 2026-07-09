import math

def co_the_an_het(pile, h, toc_do):
    thoi_gian = 0
    for chuoi in pile:
        thoi_gian += math.ceil(chuoi / toc_do)
    return thoi_gian <= h

def tim_toc_do(pile, h):
    trai = 1
    phai = max(pile)
    ket_qua = phai
    
    while trai <= phai:
        giua = (trai + phai) // 2
        if co_the_an_het(pile, h, giua):
            ket_qua = giua
            phai = giua - 1
        else:
            trai = giua + 1
            
    return ket_qua

pile = [3, 6, 7, 11]
h = 8
print(tim_toc_do(pile, h))
