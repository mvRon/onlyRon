class HocSinh:
    def __init__(self) -> None:
        self.Ho_Ten = ""
        self.Tuoi = ""
        self.Diem_Toan = ""
        self.Diem_Van = ""
        self.Diem_AV = ""

    def Nhapthontin(self):
        self.Ho_Ten = input("Nhap Ho va Ten:")
        self.Tuoi = int(input("Nhap tuoi:"))
        while True:
            self.Diem_Toan = float(input("Nhap diem toan:"))
            self.Diem_Van = float(input("Nhap diem van:"))
            self.Diem_AV = float(input("Nhap diem AV:"))
            if ((0<=self.Diem_Toan<=10) and (0<=self.Diem_Van<=10) and (0<=self.Diem_AV<=10)):
                break
            else:
                print("Diem khong hop le, moi ban nhap lai. Thang diem tu 0-10!")
    
    def Xuatthongtin(self):
        print(f"Ho va Ten: {self.Ho_Ten}")
        print(f"Tuoi: {self.Tuoi}")
        print(f"Diem Toan: {self.Diem_Toan}")
        print(f"Diem Van: {self.Diem_Van}")
        print(f"Diem AV: {self.Diem_AV}")

    def DTB(self):
        dtb = ((self.Diem_Toan*2) + (self.Diem_Van*2) + self.Diem_AV)/5
        return dtb

if __name__ == "__main__":
    call = HocSinh()
    print("Nhap thong tin")
    call.Nhapthontin()
    print("Xuat thong tin")
    call.Xuatthongtin()
    print(f"Diem trung binh: {call.DTB()}")


        