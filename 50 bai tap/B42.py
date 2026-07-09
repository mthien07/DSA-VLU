class NutBam:
    def __init__(self, khoa, gia_tri):
        self.khoa = khoa
        self.gia_tri = gia_tri
        self.tiep_theo = None

class BangBam:
    def __init__(self, kich_thuoc=10):
        self.kich_thuoc = kich_thuoc
        self.mang = [None] * kich_thuoc
        
    def _bam(self, khoa):
        return hash(khoa) % self.kich_thuoc
        
    def put(self, khoa, gia_tri):
        chi_muc = self._bam(khoa)
        if not self.mang[chi_muc]:
            self.mang[chi_muc] = NutBam(khoa, gia_tri)
            return
            
        hien_tai = self.mang[chi_muc]
        while hien_tai:
            if hien_tai.khoa == khoa:
                hien_tai.gia_tri = gia_tri
                return
            if not hien_tai.tiep_theo:
                break
            hien_tai = hien_tai.tiep_theo
            
        hien_tai.tiep_theo = NutBam(khoa, gia_tri)
        
    def get(self, khoa):
        chi_muc = self._bam(khoa)
        hien_tai = self.mang[chi_muc]
        while hien_tai:
            if hien_tai.khoa == khoa:
                return hien_tai.gia_tri
            hien_tai = hien_tai.tiep_theo
        return None

bb = BangBam()
bb.put("a", 1)
bb.put("b", 2)
print(f'get("a") -> {bb.get("a")}')
