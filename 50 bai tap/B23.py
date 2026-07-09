def tinh_rpn(bieu_thuc):
    ngan_xep = []
    tokens = bieu_thuc.split()
    
    for token in tokens:
        if token in '+-*/':
            b = ngan_xep.pop()
            a = ngan_xep.pop()
            if token == '+':
                ngan_xep.append(a + b)
            elif token == '-':
                ngan_xep.append(a - b)
            elif token == '*':
                ngan_xep.append(a * b)
            elif token == '/':
                ngan_xep.append(int(a / b))
        else:
            ngan_xep.append(int(token))
            
    return ngan_xep[0]

print(tinh_rpn('3 4 + 2 *'))
