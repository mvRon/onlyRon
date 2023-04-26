import os
file_name = input("Nhap ten file:")
folder = os.path.dirname(__file__)
if os.path.exists(file_name):
    print(f"{file_name} ton tai!")
    f = open(file_name,"r")
    nd = f.read()
    print(f"ND cua {file_name}:\n{nd}")
    f.close()
else:
    print(f"{file_name} khong ton tai!")
    