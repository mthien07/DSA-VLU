class Mang2Chieu:
    def __init__(self, so_hang, so_cot):
        self.grid = [[0]*so_cot for _ in range(so_hang)]

    def them_hang(self, hang_moi):
        self.grid.append(hang_moi)

    def set_val(self, i, j, val):
        self.grid[i][j] = val

    def get_val(self, i, j):
        return self.grid[i][j]

    def in_mang(self):
        for hang in self.grid:
            print(hang)

m = Mang2Chieu(2, 3)
m.set_val(0, 0, 5)
m.them_hang([1, 1, 1])
m.in_mang()
print("Gia tri tai (0,0):", m.get_val(0, 0))
