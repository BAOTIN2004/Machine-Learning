import numpy as np
def tinh(data):
    lst_kq=[]
    for x in data:
        kq=1/(1+np.exp(-x))
        lst_kq.append(kq)
    return lst_kq

def nhap():
    n=int(input('so gia tri trong danh sach: '))
    data=[]
    for i in range(0,n,1):
        x=int(input('nhap gia tri x: '))
        data.append(x)
    return data

data=nhap()
kq=tinh(data)
print(kq)