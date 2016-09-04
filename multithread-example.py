import sys
import threading

class safe_print(object):
    def __init__(self):
        self.mylock = threading.Lock()
    
    def prn(self,str):
        self.mylock.acquire(1)
        print str
        self.mylock.release()

class mythread(threading.Thread):
   def __init__(self,mylocalsafeprint,i):
       threading.Thread.__init__(self)
       self.mylocalsafeprint = mylocalsafeprint
       self.i=i
   def run(self):
       for j in range(0,100):
           self.mylocalsafeprint.prn(str(j)+"hello world"+str(self.i))

mysafe_print=safe_print()

mythreadlist=[]
for i in range(0,100):
   mythreadlist.append(mythread(mysafe_print,i))

for mt in mythreadlist:
    mt.start()
