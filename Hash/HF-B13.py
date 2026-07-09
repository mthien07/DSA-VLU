def hash_2d_block(ma_tran):
    chuoi_ket_hop = ""
    for hang in ma_tran:
        chuoi_ket_hop += str(hang)
    return hash(chuoi_ket_hop)

ma_tran = [[1, 2], [3, 4]]
print("Hash cua ma tran 2x2:", hash_2d_block(ma_tran))
print("Khi truot khoi, ta se ket hop xoa cot cu va them cot moi (Rabin Karp 2D).")
