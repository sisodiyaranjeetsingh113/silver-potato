import threading

def task1():
    for i in range(1,11):
        print("this is task1..!")


def task2():
    for i in range(1,11):
        print("this is task2..!")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()

for i in range(1,11):
        print("this is main..!")
