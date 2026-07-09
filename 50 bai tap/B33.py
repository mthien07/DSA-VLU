class MangDongChen:
    def __init__(self):
        self.mang = [1, 3, None, None]
        self.kich_thuoc = 2
        self.suc_chua = 4
        
    def insert(self, index, val):
        if index < 0 or index > self.kich_thuoc:
            raise IndexError("Chi so nam ngoai pham vi")
            
        for i in range(self.kich_thuoc, index, -1):
            self.mang[i] = self.mang[i - 1]
            
        self.mang[index] = val
        self.kich_thuoc += 1
        
    def hien_thi(self):
        return self.mang[:self.kich_thuoc]

md = MangDongChen()
md.insert(1, 2)
print(f"insert(1, 2) -> {md.hien_thi()}")
