class BangBamKep:
    def __init__(self, kich_thuoc=11):
        self.kich_thuoc = kich_thuoc
        self.mang = [None] * kich_thuoc
        
    def _bam1(self, khoa):
        return khoa % self.kich_thuoc
        
    def _bam2(self, khoa):
        R = 7
        return R - (khoa % R)
        
    def put(self, khoa):
        if None not in self.mang:
            print("Bang bam da day")
            return
            
        chi_muc = self._bam1(khoa)
        buoc_nhay = self._bam2(khoa)
        
        i = 0
        while True:
            chi_muc_moi = (chi_muc + i * buoc_nhay) % self.kich_thuoc
            if self.mang[chi_muc_moi] is None:
                self.mang[chi_muc_moi] = khoa
                break
            i += 1

bb = BangBamKep()
bb.put(10)
bb.put(21)
bb.put(32)

print("Mang sau khi chen (su dung Double Hashing):", bb.mang)
