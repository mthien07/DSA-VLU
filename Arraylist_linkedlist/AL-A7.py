def test_amortized(so_lan_append):
    capacity = 1
    size = 0
    tong_phep_gan = 0
    
    for i in range(so_lan_append):
        if size == capacity:
            tong_phep_gan += size 
            capacity *= 2
        tong_phep_gan += 1
        size += 1
        
    print(f"Sau {so_lan_append} lan append:")
    print(f"Tong so phep gan (sao chep + them moi): {tong_phep_gan}")
    print(f"Chi phi trung binh moi lan append: {tong_phep_gan / so_lan_append:.2f} (~ O(1))")

test_amortized(100)
