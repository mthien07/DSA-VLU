# Bai 22: Selection sort on dinh in-place

## Van de

Selection sort chuan dung swap => KHONG on dinh.

Vi du: `[(2,'a'), (2,'b'), (1,'c')]`
- Vong 1: swap `(2,'a')` va `(1,'c')` => `[(1,'c'), (2,'b'), (2,'a')]`
- `(2,'a')` va `(2,'b')` bi dao thu tu => khong on dinh.

## Cach lam on dinh

Thay vi swap, khi tim duoc min tai vi tri `min_idx`, **dich chuyen** tat ca phan tu tu `i` den `min_idx - 1` sang phai 1 vi tri, roi dat min vao vi tri `i`.

```
min_val = a[min_idx]
for k in range(min_idx, i, -1):
    a[k] = a[k-1]
a[i] = min_val
```

Cach nay giu nguyen thu tu tuong doi cua cac phan tu bang nhau => **on dinh**.

## Danh doi

- **Uu diem**: On dinh, in-place (O(1) bo nho phu)
- **Nhuoc diem**: So thao tac dich chuyen tang len O(n^2) (thay vi toi da n-1 swap)
- Selection sort chuan: toi da `n-1` swap
- Selection sort on dinh: toi da `n(n-1)/2` shift

=> Phai danh doi giua **tinh on dinh** va **so thao tac di chuyen**.
