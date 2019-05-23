import matplotlib.pyplot as plt

#ploting first line
x1=[1,2,3]
y1=[1,2,3]
plt.plot(x1,y1,label='line1')


#ploting  second line
x2=[4,5,6]
y2=[2,1,0]
plt.plot(x2,y2,label='line2')

#labeling x and y axis

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two line graph')
plt.show()
    
