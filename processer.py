import threading
import subprocess

class reader(threading.Thread):
    def __init__(self,process):
       threading.Thread.__init__(self)
       self.process = process
    def run(self):
        fs = self.process.stdout
        while True:
            rl = fs.readline()
            if rl == '':
                break
            print rl


p = subprocess.Popen(["ls"],stdout=subprocess.PIPE)
r = reader(p)
r.start()
r.join()


    
