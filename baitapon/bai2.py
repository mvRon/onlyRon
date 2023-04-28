from bai1 import bai1_tinhS, bai2_tinhY
import os
file_name = input("Nhap ten file:")
folder = os.path.dirname(__file__)
file = folder+"\\"+file_name
# print(file)
if os.path.exists(file):
    print(f"{file_name} ton tai!")
    f = open(file,"w")
    kq_1a = bai1_tinhS(x=int(input("Nhap x:")),n=int(input("Nhap n:")))
    kq_1b = bai2_tinhY(number=int(input("Nhap x:")))
    f.write(f"Ket qua cau 1a: {kq_1a}\nKet qua cau 1b: {kq_1b}")
    f.close()
    print("Luu ket qua hoan tat!")
    f = open(file,"r")
    nd = f.read()
    f.close()
    print(f"Noi dung cua {file_name}:\n{nd}")
else:
    f = open(file,"x")
    print(f"{file_name} khong ton tai!")
    print(f"Tao moi {file_name} hoan tat")
    f = open(file,"w")
    kq_1a = bai1_tinhS(x=int(input("Nhap x:")),n=int(input("Nhap n:")))
    kq_1b = bai2_tinhY(number=int(input("Nhap x:")))
    f.write(f"Ket qua cau 1a: {kq_1a}\nKet qua cau 1b: {kq_1b}")
    f.close()
    print("Luu hoan tat!")
    f = open(file,"r")
    nd = f.read()
    f.close()
    print(f"Noi dung vua moi ghi:\n{nd}")


