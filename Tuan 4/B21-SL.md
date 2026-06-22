# Bai 21: Chung minh so so sanh cua Selection Sort luon co dinh

## Menh de

Selection sort luon thuc hien dung `n(n-1)/2` phep so sanh, khong phu thuoc dau vao.

## Chung minh

Vong lap ngoai chay voi `i = 0, 1, ..., n-2` (tong `n-1` vong).

Tai moi vong thu `i`, vong lap trong duyet tu `j = i+1` den `j = n-1` de tim min.

So phep so sanh tai vong thu `i` = `n - 1 - i`.

Tong so sanh:

```
S = (n-1) + (n-2) + ... + 1 = n(n-1)/2
```

Khong co dieu kien `break` hay dung som => so sanh **luon** la `n(n-1)/2` bat ke mang da sap xep, ngau nhien hay sap nguoc.

=> **Khong co best case nhanh hon.** Selection sort luon O(n^2) ve so sanh.

**Q.E.D.**
