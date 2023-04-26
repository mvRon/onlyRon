def tongchan(ds):
    tong = 0
    for i in range(len(ds)):
        if ds[i]%2==0:
            tong += ds[i]
    return tong

ds = [1,2,3,6,3,5,1,9,0,15,66]
print(f"Tong cac so chan la: {tongchan(ds)}")