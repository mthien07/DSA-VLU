#Cau 7 (Bang bam & Mang cong don)
#Cho mang so nguyen A = [3, 4, 7, 2, -3, 1, 4, 2] va muc tieu S = 7. 
# Viec dung 2 vong lap long nhau de dem mang con co tong bang S se ton O(N^2). 
# Hay trinh bay phuong phap toi uu hon su dung Bang bam (Hash Map) ket hop Mang cong don (Prefix Sum) de giai quyet trong O(N). 
# Co bao nhieu mang con thoa man trong mang A da cho

"""
Phuong phap toi uu O(N):
- Su dung Mang cong don (Prefix Sum): Goi prefix_sum[i] la tong cac phan tu tu A[0] den A[i].
  Tong cua mot mang con tu chi so i den j (i <= j) se la: sum(i, j) = prefix_sum[j] - prefix_sum[i-1].
- Muc tieu la tim so luong mang con co tong bang S, tuc la: prefix_sum[j] - prefix_sum[i-1] = S 
  => prefix_sum[i-1] = prefix_sum[j] - S.
- Dung Bang bam (Hash Map): Luu tru tan suat xuat hien cua cac gia tri prefix_sum da duyet qua.
  Khi duyet den phan tu thu j va tinh duoc prefix_sum[j]:
  + Ta kiem tra xem (prefix_sum[j] - S) da xuat hien trong bang bam chua. 
  + Neu co, so lan xuat hien cua no chinh la so luong mang con ket thuc tai j co tong bang S.
  + Cong so luong nay vao ket qua dem.
  + Cap nhat tan suat cua prefix_sum[j] vao bang bam.
- Khoi tao bang bam voi gia tri {0: 1} de tinh truong hop mang con bat dau ngay tu vi tri dau tien (A[0]).
"""

A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7

def count_subarray_sum(A, S):
    prefix_counts = {0: 1}
    current_sum = 0
    count = 0
    
    for num in A:
        current_sum += num
        if current_sum - S in prefix_counts:
            count += prefix_counts[current_sum - S]
        if current_sum in prefix_counts:
            prefix_counts[current_sum] += 1
        else:
            prefix_counts[current_sum] = 1       
    return count

res = count_subarray_sum(A, S)
print(res)
