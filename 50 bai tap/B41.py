class NutKep:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DanhSachLienKetKep:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def chen_cuoi(self, val):
        nut = NutKep(val)
        if not self.head:
            self.head = self.tail = nut
        else:
            self.tail.next = nut
            nut.prev = self.tail
            self.tail = nut
        return nut
            
    def xoa_nut(self, nut):
        if not nut:
            return
            
        if nut.prev:
            nut.prev.next = nut.next
        else:
            self.head = nut.next
            
        if nut.next:
            nut.next.prev = nut.prev
        else:
            self.tail = nut.prev
            
    def in_danh_sach(self):
        ket_qua = []
        hien_tai = self.head
        while hien_tai:
            ket_qua.append(str(hien_tai.val))
            hien_tai = hien_tai.next
        print(" <-> ".join(ket_qua))

dl = DanhSachLienKetKep()
nut_a = dl.chen_cuoi('A')
nut_b = dl.chen_cuoi('B')
nut_c = dl.chen_cuoi('C')

print("Truoc khi xoa:")
dl.in_danh_sach()

dl.xoa_nut(nut_b)

print("Sau khi xoa B:")
dl.in_danh_sach()
