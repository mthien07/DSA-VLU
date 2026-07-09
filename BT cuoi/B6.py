#Cau 6 (Danh sach lien ket - Linked List)
#Khi phat hien chu trinh trong danh sach lien ket bang thuat toan Floyd (Rua chay 1 buoc, Tho chay 2 buoc), hai con tro se gap nhau tai mot diem nam trong chu trinh. 
#Sau do, thuat toan dua 1 con tro ve lai Node dau tien (Head), ca 2 con tro cung di moi nhip 1 buoc thi chung se gap nhau tai chinh xac nut bat dau chu trinh. 
#Hay giai thich nguyen ly toan hoc dang sau giai doan 2 nay

"""
Giai thich nguyen ly toan hoc:
Goi:
- L: Khoang cach tu Node dau tien (Head) den nut bat dau chu trinh.
- C: Chieu dai cua chu trinh (so luong Node trong chu trinh).
- K: Khoang cach tu nut bat dau chu trinh den diem gap nhau cua Rua va Tho.

Khi Rua va Tho gap nhau:
- Quang duong Rua di duoc: S_rua = L + K
- Quang duong Tho di duoc: S_tho = L + K + n*C (voi n la so vong Tho da chay quanh chu trinh truoc khi gap Rua)

Vi van toc cua Tho gap 2 lan Rua, nen trong cung mot khoang thoi gian, quang duong Tho di gap doi Rua:
S_tho = 2 * S_rua
=> L + K + n*C = 2 * (L + K)
=> L + K = n*C
=> L = n*C - K 
=> L = (n - 1)*C + (C - K)

Y nghia cua phuong trinh L = (n - 1)*C + (C - K):
- (C - K) chinh la khoang cach tu diem gap nhau hien tai di tiep den nut bat dau chu trinh.
- Dieu nay co nghia la, neu mot con tro xuat phat tu Head (can di quang duong L de den nut bat dau chu trinh) 
  va mot con tro xuat phat tu diem gap nhau (can di quang duong C - K, va them n-1 vong chu trinh nua de ve nut bat dau chu trinh),
  khi ca 2 cung di chuyen moi buoc 1 Node, chung se gap nhau chinh xac tai nut bat dau chu trinh.
"""
