def kiemtra_nt(number):
    if number<2:
        return False
    else:
        for i in range(2,number):
            if number%i==0:
                return False
        return True
    

def Count(num):
    if num==0:
        return 0
    else:
        return 1 + Count(num//10)

  
if __name__ == "__main__":
    number = int(input("Nhap vao 1 so:"))
    if kiemtra_nt(number)==True:
        print(f"{number} la so nguyen to!")
    else:
        print(f"{number} khong phai la so nguyen to!")
    
    num = int(input("Nhap day so nguyen:"))
    print(f"{num} co {Count(num)} chu so!")
    
            