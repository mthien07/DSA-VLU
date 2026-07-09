class MangDongXoa:
    def __init__(self):
        self.mang = [1, 2, 3]
        self.kich_thuoc = 3
        
    def remove(self, index):
        if index < 0 or index >= self.kich_thuoc:
            raise IndexError("Chi so nam ngoai pham vi")
            
        for i in range(index, self.kich_thuoc - 1):
            self.mang[i] = self.mang[i + 1]
            
        self.mang[self.kich_thuoc - 1] = None
        self.kich_thuoc -= 1
        
    def hien_thi(self):
        return self.mang[:self.kich_thuoc]

md = MangDongXoa()
md.remove(0)
print(f"remove(0) -> {md.hien_thi()}")
