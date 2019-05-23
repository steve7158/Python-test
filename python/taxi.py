print 'input the no of grps'
n=input()
n=int(n)
print type(n)
a=[]
i=0
for obj in range(n):
    mem=input('enter the no of members in this grp')
    mem=int(mem)
    a.append(mem)

print a
print type(a)
taxi=0
print '========================='
for obj in a:
    j=i+1
    vacancy=4-obj
    print 'obj: %d vpacancy: %d'%(obj,vacancy)
    if vacancy==0:
        print 'in 0 conditio'
        taxi=taxi+1
        print taxi
    else:
        k=j
        for rem in a[j:]:

            print '\n---------------\nthe value of the counter j %d \n---------------' %(k)
            if rem<=vacancy:
                print '\n \t------------------------\n \tinside the if condition'
                # taxi=taxi+1
                a[k]=0
                vacancy=vacancy-rem
                print '\tvacancy: %d \n \t-------------------------\n'%(vacancy)
            k=k+1
        taxi=taxi+1
        print 'the no of taxi so far : %d' %(taxi)
    i=i+1


print 'the number of taxi required are: %d'%(taxi)
