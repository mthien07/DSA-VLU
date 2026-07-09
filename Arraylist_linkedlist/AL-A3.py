class ArrayList:
    def __init__(self):
        self.items = []

    def insertAt(self, index, val):
        if index < 0 or index > len(self.items):
            print("Loi: Chi so khong hop le!")
            return
        self.items.insert(index, val)

    def removeAt(self, index):
        if index < 0 or index >= len(self.items):
            print("Loi: Chi so khong hop le!")
            return None
        return self.items.pop(index)

al = ArrayList()
al.insertAt(0, 1); al.insertAt(1, 2); al.insertAt(2, 4)
print("Truoc khi chen:", al.items)
al.insertAt(2, 3)
print("Sau khi chen 3 vao index 2:", al.items)
