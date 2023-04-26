class NhanVien:
    def __init__(self) -> None:
        self.Manv = ""
        self.Ho_Ten = ""
        self.Tuoi = ""
        self.Gioi_Tinh = ""
        self.luong = ""

    def Nhapthongtin(self):
        self.Manv = input("Nhap ma nhan vien:")
        self.Ho_Ten = input("Nhap ho va ten nhan vien:")
        while True:
            self.Tuoi = int(input("Nhap tuoi nhan vien:"))
            if self.Tuoi>=18:
                break
            else:
                print("Tuoi ban nhap khong dung, moi nhap lai!")
        self.Gioi_Tinh = input("Nhap gioi tinh nhan vien:")
        self.luong = float(input("Nhap luong nhan vien:"))

    def Xuatthongtin(self):
        print(f"Ma NV: {self.Manv}")
        print(f"Ho va ten: {self.Ho_Ten}")
        print(f"Tuoi: {self.Tuoi}")
        print(f"Gioi tinh: {self.Gioi_Tinh}")
        print(f"Luong: {self.luong}")
        
    def TinhTienThue(self):
        self.thue = 0
        if self.luong>=20000000:
            self.thue = (self.luong - 11000000)*0.2
            return self.thue
        elif self.luong>=15000000 and self.luong<20000000:
            self.thue = (self.luong - 11000000)*0.1
            return self.thue
        elif self.luong<15000000 and self.luong>0:
            return self.thue
        else:
            pass
        
        


if __name__ == "__main__":
    call = NhanVien()
    print("Nhap thong tin")
    call.Nhapthongtin()
    print("Xuat thong tin")
    call.Xuatthongtin()
    print(f"Thue phai tra la: {call.TinhTienThue()}")