from threading import Thread
import time
i=0
def getnumber(Thread):
    while(True):
            i=i+1

def squaring(Thread):
    while(True):
        i=i**2
        print(i)

t1=getnumber()
t2=squaring()

     # t1=threading.Thread(target=getnumber)
     # t2=threading.Thread(target=squaring)
 t1.start()
 t2.start()
     # t1.join()
     # t2.join()

 print('done')
