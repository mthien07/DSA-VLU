# Tuan 1

## Phan A

Câu 1
-Input: Nhận vào 1 tập dữ liệu, không bắt buộc phải sắp xếp theo thứ tự
-Output: Trả về vị trí của phần tử trong mảng nếu phần tử đó khớp với khóa key. Nếu tìm không thấy key trong mảng, thuật toán sẽ trả về kết quả "không tìm thấy"
-Thuật toán sẽ dừng lại vào 2 trường hợp sau:
1. Tìm thấy phần tử thành công
2. Duyệt hết danh sách
Câu 2
Bước    Chỉ số      Giá trị A[i]    So sánh(x = 5)     Kết luận
--------------------------------------------------------------------------------------
1       i = 0       A = 7           7 /= 5              Không khớp chỉ số i tăng lên 1
2       i = 1       A = 3           3 /= 5              Không khớp chỉ số i tăng lên 1
3       i = 2       A = 9           5 /= 5              Không khớp chỉ số i tăng lên 1
4       i = 3       A = 12          12 /= 5             Không khớp chỉ số i tăng lên 1
5       i = 4       A = 5           5 = 5               Tìm thấy dừng thuật toán
Giá trị hàm trả về: Thuật toán sẽ kết thúc ở bước 5 và trả về giá trị 4
Câu 3
a/ Tìm x = 7
-Phần tử 7 nằm ngay vị trí đầu mảng
-Thuật toán dừng ngay lập tức
b/ Tìm x = 1
-Phần tử 1 nằm ở vị trí cuối bảng
-Thuật toán lần lượt so sánh các giá trị trong mảng cho đến phần tử cuối cùng
c/ Tìm x = 100
-Vì 100 không tồn tại trong mảng, thuật toán bắt buộc phải duyệt và so sánh x với toàn bộ 7 phần tử của mảng. Sau khi kiểm tra đến phần tử cuối cùng mà vẫn không thấy, nó kết luận là "không tìm thấy"
Câu 4
-Trường hợp tốt nhất: Xảy ra khi phần tử cần tìm nằm ngay vị trí đầu tiên của mảng. Lúc này, thuật toán tìm thấy giá trị khớp ngay ở bước đầu tiên nên số phép so sánh là 1
-Trường hợp xấu nhất: Xảy ra khi phần tử cần tìm nằm ở vị trí cuối cùng hoặc hoàn toàn không có mặt trong mảng. Thuật toán bắt buộc phải duyệt và kiểm tra qua toàn bộ các phần tử cho đến khi kết thúc danh sách, do đó số phép so sánh đạt mức tối đa là n
-Trường hợp trung bình: Giả định phần tử cần tìm chắc chắn có trong mảng và xác suất nó nằm ở bất kỳ vị trí nào (từ vị trí thứ 1 đến vị trí thứ n) là ngang nhau. Khi đó, số phép so sánh trung bình sẽ là trung bình cộng của số phép so sánh tại mọi vị trí
Câu 5
-Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước vì thuật toán hoạt động bằng cách duyệt tuần tự từ phần tử đầu tiên và so sánh lần lượt cho đến khi hết danh sách, nên việc mảng có thứ tự hay không không ảnh hưởng đến logic của thuật toán
-Tìm kiếm tuyến tính: Có thể áp dụng cho tập dữ liệu bất kỳ, dù đã được sắp xếp hay chưa
-Tìm kiếm nhị phân: Bắt buộc chỉ áp dụng đối với dãy số đã có thứ tự

## Phan B - Cau6

```python
def linearsearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
```

## Phan B - Cau7

```python
def ton_tai(a, x):
    for i in range (len(a)):
        if a[i] == x:
            return True
    return False
```

## Phan B - Cau 8

```python
def dem_xuat_hien(a, x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            dem += 1
    return dem
```

## Phan B - Cau 9

```python
def tim_tat_ca(a, x):
    danh_sach = []
    for i in range(len(a)):
        if a[i] == x:
            danh_sach.append(i)
    return danh_sach
```

## Phan B - Cau 10

```python
def xuat_hien_cuoi_cung(a, x):
    for i in range(len(a)-1, -1, -1):
        if a[i] == x:
            return i
    return -1
def xuat_hien_cuoi_cung_2(a, x):
    vi_tri_cuoi = -1
    for i in range(len(a)):
        if a[i] == x:
            vi_tri_cuoi = i
    return vi_tri_cuoi
```

## Phan B - Cau 11

```python
def gtln(a):
    if len(a) == 0:
        return None
    vt_max = 0
    gt_max = a
    for i in range(1, len(a)):
        if a[i] > gt_max:
            gt_max = a[i]
            vt_max = i
    return vt_max
```

## Phan B - Cau 12

```python
def min_max(a):
    if len(a) == 0:
        return None
    vt_min = vt_max = 0
    gt_min = gt_max = a[0]
    for i in range(1, len(a)):
        if a[i] < gt_min:
            gt_min = a[i]
            vt_min = i
        elif a[i] > gt_max:
            gt_max = a[i]
            vt_max = i
    return gt_min, vt_min, gt_max, vt_max
```

## Phan C - Cau 13

```python
def tim_ten(ds, ten):
    ten_chuan = ten.strip().lower()
    for i in range(len(ds)):
        if ds[i].strip().lower() == ten_chuan:
            return i
    return -1
```

## Phan C - Cau 14

```python
def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1
a = [ ]
vi_tri = tim_so_chan_dau_tien(a)
if vi_tri != -1:
    print(f"so chan {a[vi_tri]} tai {[vi_tri]}")
else:
    print("khong co so chan")
```

## Phan C - Cau 15

```python
import math
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if so_nguyen_to(a[i]):
            return a[i], i
    return -1, -1
```

## Phan C - Cau 16

```python
def tim_phan_tu_gan_nhat(a, x):
    if len(a) == 0:
        return None, -1
    vt_min = 0
    khoang_cach_min = abs(a - x)
    for i in range(1, len(a)):
        khoang_cach_hien_tai = abs(a[i] - x)
        
        if khoang_cach_hien_tai < khoang_cach_min:
            khoang_cach_min = khoang_cach_hien_tai 
            vt_min = i
    return a[vt_min], vt_min
```

## Phan C - Cau 17

```python
def sentinel_linear_search(a, x):
    n = len(a)
    a.append(x) 
    i = 0
    while a[i] != x:
        i += 1
    a.pop()
    if i < n:
        return i
    else:
        return -1
```

## Phan C - Bai 18

```python
def linear_search_matrix(M, x):
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == x:
                return (i, j)
    return (-1, -1)
```

## Phan C - Cau 19

```python
danh_sach_sv = [
    {"ma_sv": "SV001", "ho_ten": "Nguyen Van A", "dtb": 8.5},
    {"ma_sv": "SV002", "ho_ten": "Tran Thi B", "dtb": 7.2},
    {"ma_sv": "SV003", "ho_ten": "Le Van C", "dtb": 9.0},
    {"ma_sv": "SV004", "ho_ten": "Pham Thi D", "dtb": 6.8}
]
def tim_sinh_vien(danh_sach, ma_sv_can_tim):
    for sv in danh_sach:
        if sv["ma_sv"] == ma_sv_can_tim:
            print(f"msv: {sv['ma_sv']}")
            print(f"Ho va ten: {sv['ho_ten']}")
            print(f"Diemtb: {sv['dtb']}")
            return
    print(f"khong tim thay {ma_sv_can_tim}")
```

## Phan C - Cau 20

```python
danh_ba = []
def them_lien_he(ten, sdt):
    lien_he = {"ten": ten, "sdt": sdt}
    danh_ba.append(lien_he)
    print(f"da them lien he: {ten} - {sdt}")
def tim_sdt_theo_ten(ten_can_tim):
    for lh in danh_ba:
        if lh["ten"].lower() == ten_can_tim.lower():
            return lh["sdt"]
    return None
def tim_ten_theo_sdt(sdt_can_tim):
    for lh in danh_ba:
        if lh["sdt"] == sdt_can_tim:
            return lh["ten"]
    return None
def dem_lien_he_theo_dau_so(dau_so):
    dem = 0
    for lh in danh_ba:
        if lh["sdt"].startswith(dau_so):
            dem += 1
    return dem
def menu():
    while True:
        print("\n" + "="*30)
        print("Danh ba")
        print("1. them lien he moi")
        print("2. tim sdt theo ten")
        print("3. tim ten theo sdt")
        print("4. dem so lien he")
        print("5. xem danh ba")
        print("0. exit")
        print("="*30)
        
        chon = input("nhap chuc nang (0-5)): ")
        
        if chon == '1':
            ten = input("nhap ten: ")
            sdt = input("nhap sdt: ")
            them_lien_he(ten, sdt)
            
        elif chon == '2':
            ten = input("nhap ten can tim: ")
            ket_qua = tim_sdt_theo_ten(ten)
            if ket_qua:
                print(ket_qua)
            else:
                print(ten)
                
        elif chon == '3':
            sdt = input("nhap sdt: ")
            ket_qua = tim_ten_theo_sdt(sdt)
            if ket_qua:
                print(ket_qua)
            else:
                print(sdt)
        elif chon == '4':
            dau_so = input("nhap sdt can dem: ")
            so_luong = dem_lien_he_theo_dau_so(dau_so)
            print(f"{so_luong} lien he co so '{dau_so}'")
            
        elif chon == '5':
            print("\ndanh sach:")
            if len(danh_ba) == 0:
                print("danh ba trong")
            else:
                for i, lh in enumerate(danh_ba, 1):
                    print(f"{i}. {lh['ten']} - {lh['sdt']}")
                    
        elif chon == '0':
            print("bai")
            break
        else:
            print("thu lai")
if __name__ == "__main__":
    menu()
```

