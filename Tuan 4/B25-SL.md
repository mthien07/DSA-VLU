# Bai 25: Chung minh tinh dung dan cua Selection Sort (Loop Invariant)

## Bat bien vong lap (Loop Invariant)

> Sau vong lap thu `i` (voi `i = 0, 1, ..., n-2`):
> Doan `a[0..i]` chua `i+1` phan tu nho nhat cua mang ban dau, da duoc sap xep tang dan.

---

## Chung minh

### 1. Khoi tao (Initialization)

Truoc vong lap dau tien (`i = 0`), chua co phan tu nao duoc dat.

Doan rong `a[0..-1]` thoa man bat bien mot cach tam thuy (vacuously true).

=> Bat bien dung.

---

### 2. Duy tri (Maintenance)

Gia su bat bien dung sau vong lap thu `i-1`: `a[0..i-1]` chua `i` phan tu nho nhat, da sap xep.

Vong lap thu `i`:

1. Tim `min_idx` = chi so phan tu nho nhat trong doan `a[i..n-1]`
2. Hoan doi `a[i]` va `a[min_idx]`

Sau buoc nay:

- `a[i]` la phan tu nho nhat trong `a[i..n-1]`, tuc la phan tu nho thu `i+1` cua mang
- Vi `a[0..i-1]` da chua `i` phan tu nho nhat va da sap xep, va `a[i] >= a[i-1]`
- => `a[0..i]` chua `i+1` phan tu nho nhat, da sap xep

=> Bat bien dung sau vong lap thu `i`.

---

### 3. Ket thuc (Termination)

Vong lap ket thuc khi `i = n-1`.

Theo bat bien: `a[0..n-2]` chua `n-1` phan tu nho nhat, da sap xep.

Phan tu con lai `a[n-1]` la phan tu lon nhat => dung vi tri.

=> Toan bo mang `a[0..n-1]` da sap xep tang dan. Thuat toan DUNG va DUNG.

**Q.E.D.**
