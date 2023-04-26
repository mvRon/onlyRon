def kiemtra_cp(n):
    for i in range(int(n)):
        if i**2==n:
            return True
    return False

def tongbieuthuc(number):
    if number==0:
        return 2
    else:
        return ((2*number +2) + tongbieuthuc(number - 1))
if __name__ == "__main__":
    n = float(input("Nhap N:"))
    print(f"Kiem tra so chinh phuong: {kiemtra_cp(n)}")

    number = int(input("Nhap Number:"))
    print(f"Ket qua la: {tongbieuthuc(number)}")