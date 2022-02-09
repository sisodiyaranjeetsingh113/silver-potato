import threading
class myThread(threading.Thread):
    def test(self):
        super().start()
    def run(self):
        for i in range(1,11):
            print("child...")

t1=myThread()
t1.test()

for i in range(1,11):
    print("main...")


