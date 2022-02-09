#mothed overriding is also the example of polymorphism...
class Android:
    def camera(self):
        print("3 mpx.....!!")

class Nokia(Android):
    def camera(self):
        print("4 mpx.....!!")
        s.camera()

class LG(Android):
    def camera(self):
        print("5 mpx.....!!")

class Sumsung(Android):
    def camera(self):
        print("7 mpx.....!!")

a=Android()
n=Nokia()
l=LG()
s=Sumsung()
a.camera()
n.camera()
l.camera()
