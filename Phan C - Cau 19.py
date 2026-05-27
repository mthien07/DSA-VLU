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