import threading
import time
class myThread(threading.Thread):
    def run(self):
        for i in range(1,6):
            time.sleep(0.2)
            print("child..!")
    

t1=myThread()
t1.start()


for i in range(1,6):
    time.sleep(0.5)
    print("main...")

    

