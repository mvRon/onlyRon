def bai1_tinhS(x, n): #Bai 1a
    if n == 0:
        return 0
    else:
        return ((-1)**(n+1))*(x**n) + bai1_tinhS(x, n-1)

def bai2_tinhY(number): #Bai 1b
    from math import sqrt
    tu_so = sqrt((4*number**2 + 4*number + 1)) * (number**2 - 8*number + 16)
    mau_so = number**2 - 16
    try:
        bieu_thuc = tu_so/mau_so
        return bieu_thuc
    except:
        print("Mau so phai khac 0 !")    

    

if __name__ == "__main__":
    x = int(input("Nhập giá trị x(Bai 1a): "))
    n = int(input("Nhập giá trị n(Bai 1a): "))

    print("Kết quả của S(x,n) là:", bai1_tinhS(x,n))
    
    number = int(input("Nhap gia tri X(Bai 1b):"))
    if bai2_tinhY(number)==None:
        print(f"Bieu thuc khong xac dinh!")
    else:
        print(f"Ket qua bieu thuc Y = {bai2_tinhY(number)}")