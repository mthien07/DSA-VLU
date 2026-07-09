print("Thuc nghiem:")
khoa = [10, 20, 30, 40, 50]

print("Voi m = 10 (khong la so nguyen to):")
for k in khoa:
    print(f"{k} % 10 = {k % 10}")
print("=> Tat ca deu roi vao bucket 0!")

print("\nVoi m = 11 (so nguyen to):")
for k in khoa:
    print(f"{k} % 11 = {k % 11}")
print("=> Phan bo deu hon cac bucket khac nhau.")
