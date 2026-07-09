class ArrayList:
    def __init__(self):
        self.items = []
        self.modCount = 0

    def append(self, val):
        self.items.append(val)
        self.modCount += 1

    def getIterator(self):
        return Iterator(self)

class Iterator:
    def __init__(self, danh_sach):
        self.danh_sach = danh_sach
        self.expectedModCount = danh_sach.modCount
        self.hien_tai = 0

    def hasNext(self):
        return self.hien_tai < len(self.danh_sach.items)

    def next(self):
        if self.expectedModCount != self.danh_sach.modCount:
            print("Loi: Danh sach bi sua doi trong khi dang duyet (Fail-Fast)!")
            return None
        val = self.danh_sach.items[self.hien_tai]
        self.hien_tai += 1
        return val

al = ArrayList()
al.append(1); al.append(2)

it = al.getIterator()
print(it.next())

al.append(3)

print(it.next())
