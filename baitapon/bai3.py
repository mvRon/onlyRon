class TamGiac:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def NuaCV(self):
        self.p = (self.a + self.b + self.c)/2
        return self.p
    
    def CV(self):
        self.cv = self.a + self.b + self.c
        return self.cv
    
    def DT(self):
        from math import sqrt
        if ((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)):
            self.dt = sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))
            return self.dt
    



class TestTamGiac:
    # def __init__(self) -> None:
    #     pass
    
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    Tamgiac = TamGiac(a, b, c)
    
    
    print("Chu vi tam giác:", Tamgiac.CV())
    print("Nửa chu vi tam giác:", Tamgiac.NuaCV())
    if Tamgiac.DT()==None:
        print("Do dai 3 canh khong hop le, khong co dien tich! ")
    else:
        print("Diện tích tam giác:", Tamgiac.DT())
    

if __name__ == "__main__":
    call = TestTamGiac()
