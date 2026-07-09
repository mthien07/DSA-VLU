class MangDong:
    def __init__(self):
        self.kich_thuoc = 0
        self.suc_chua = 1
        self.mang = [None] * self.suc_chua
        
    def _tang_kich_thuoc(self):
        self.suc_chua *= 2
        mang_moi = [None] * self.suc_chua
        for i in range(self.kich_thuoc):
            mang_moi[i] = self.mang[i]
        self.mang = mang_moi
        
    def append(self, val):
        if self.kich_thuoc == self.suc_chua:
            self._tang_kich_thuoc()
        self.mang[self.kich_thuoc] = val
        self.kich_thuoc += 1
        
    def get_capacity(self):
        return self.suc_chua

md = MangDong()
for i in range(5):
    md.append(i)
print(f"append 5 phan tu -> capacity = {md.get_capacity()}")
