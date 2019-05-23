import numpy as np

'''
def zero(a):
    d=[]
    
    print type(d)
    for obj in range(a[2]):
        e=np.zeros((a[0],a[1]),dtype=np.int)
        e=e.tolist()
        print type(e)
        d.append(e)
    return d
'''
def zero(a):
    a=np.array(a,int)
    c=[]
    for i in range(a[2]):
        b=np.zeros((a[0],a[1]), dtype=np.int)
        b=b.tolist()
        #b=np.reshape(b,(a[0],a[1]))
        c.append(b)
    return c
#def one(a):


#a=raw_input().strip().split(' ')
a = tuple(map(int, input().split(' ')))
#a=np.array([[1,2],[3,4]], int)
#list(a)
#print type(a)
#a=a.tolist()
#print type(a)

#d=zero(a)
'''
c=[]
for obj in a:
    b=int(obj)
    c.append(b)
'''
d=zero(a)
for obj in d:
#    for sobj in obj:
        print obj



