class HCN:
    def __init__(self, dai, rong) -> None:
        self.dai = dai
        self.rong = rong

    def CV(self):
        return (self.dai + self.rong)*2

    def DT(self):
        return self.dai*self.rong


dai = float(input("Nhap chieu dai HCN:"))
rong = float(input("Nhap chieu rong HCN:"))
call = HCN(dai, rong)
print(f"Chu vi HCN: {call.CV()}")
print(f"Dien tich HCN: {call.DT()}")



        