class ArrayList:
    def __init__(self):
        self.items = []
    def append(self, val):
        self.items.append(val)
    def popBack(self):
        if len(self.items) == 0:
            print("sai roi m")
            return None
        return self.items.pop()

al = ArrayList()
al.append(1); al.append(2); al.append(3)
print("Ban dau:", al.items)
gia_tri_xoa = al.popBack()
print("Pop:", gia_tri_xoa)
print("Sau khi popBack:", al.items)
