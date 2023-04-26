import os
import bt2
file_name = input("Nhap ten file:")
f = open(file_name, "r")
word_list = f.read()
word_list = word_list.split()
f.close()
count = 0
number_list = []
for word in word_list:
        try:
            number = int(word)
            if number>=0:
                number_list.append(number)
        except:
            pass
for num in number_list:
    if bt2.kiemtra_cp(num)==True:
        count +=1
    else:
        continue
print(number_list)
print(f"Co {count} so chinh phuong trong {file_name}")