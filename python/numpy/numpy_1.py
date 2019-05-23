import numpy as np

def trans(arr):
    a=np.array(arr,int)
    a=np.reshape(arr[2::],(arr[0],arr[1]))
    a=np.transpose(a)
    return a

arr=raw_input().strip().split(' ')
a=trans(arr)
print a

