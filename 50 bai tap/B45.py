def kiem_tra_isomorphic(s, t):
    if len(s) != len(t):
        return False
        
    anh_xa_s_t = {}
    anh_xa_t_s = {}
    
    for char_s, char_t in zip(s, t):
        if char_s in anh_xa_s_t:
            if anh_xa_s_t[char_s] != char_t:
                return False
        else:
            anh_xa_s_t[char_s] = char_t
            
        if char_t in anh_xa_t_s:
            if anh_xa_t_s[char_t] != char_s:
                return False
        else:
            anh_xa_t_s[char_t] = char_s
            
    return True

print(kiem_tra_isomorphic("egg", "add"))
print(kiem_tra_isomorphic("foo", "bar"))
