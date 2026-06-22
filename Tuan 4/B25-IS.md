# Bai 25: Chung minh tinh dung dan cua Insertion Sort (Loop Invariant)

## Bat bien vong lap (Loop Invariant)

> Truoc moi vong lap ngoai thu `i` (voi `i = 1, 2, ..., n-1`):
> Doan `a[0..i-1]` chua **dung** cac phan tu ban dau cua `a[0..i-1]` nhung **da duoc sap xep** tang dan.

---

## Chung minh

### 1. Khoi tao (Initialization)

Truoc vong lap dau tien (`i = 1`), doan `a[0..0]` chi co 1 phan tu.

Mot phan tu luon duoc coi la da sap xep.

=> Bat bien dung.

---

### 2. Duy tri (Maintenance)

Gia su bat bien dung truoc vong lap thu `i`: `a[0..i-1]` da sap xep tang dan.

Than vong lap thuc hien:

1. Lay `key = a[i]`
2. Dich chuyen cac phan tu `a[j] > key` sang phai 1 vi tri (voi `j` di tu `i-1` ve `0`)
3. Chen `key` vao vi tri `j+1`

Sau buoc nay:

- `a[0..i]` chua dung cac phan tu ban dau cua `a[0..i]` (chi thay doi vi tri, khong them/xoa)
- `a[0..i]` da duoc sap xep (vi `key` duoc chen dung vi tri giua cac phan tu nho hon va lon hon no)

=> Bat bien dung cho vong lap thu `i+1`.

---

### 3. Ket thuc (Termination)

Vong lap ket thuc khi `i = n`.

Theo bat bien: `a[0..n-1]` chua dung cac phan tu ban dau nhung da duoc sap xep tang dan.

=> Toan bo mang da sap xep. Thuat toan DUNG.

**Q.E.D.**
