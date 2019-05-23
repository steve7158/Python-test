inp=input('enter the no of feilds to filled x position y position')
a=[]
a=inp.split(' ')
b=[]
for obj in a:
    obj=int(obj)
    b.append(obj)
no=b[0]
x=b[1]
y=b[2]
print(no,x,y)
