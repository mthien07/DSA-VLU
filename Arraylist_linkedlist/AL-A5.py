class ArrayList:
    def __init__(self):
        self.items = []
        
    def append(self, val):
        self.items.append(val)

    def duyet_va_dem_chan(self):
        dem = 0
        print("Cac phan tu trong danh sach:", end=" ")
        for val in self.items:
            print(val, end=" ")
            if val % 2 == 0:
                dem += 1
        print()
        return dem

al = ArrayList()
for i in [1, 2, 3, 4]:
    al.append(i)

so_chan = al.duyet_va_dem_chan()
print("So luong so chan:", so_chan)
