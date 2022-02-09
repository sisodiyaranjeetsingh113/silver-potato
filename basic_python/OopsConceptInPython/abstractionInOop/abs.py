from abc import ABC,abstractmethod
class Remote(ABC):
    @abstractmethod
    def ch_plus(self):
        pass
    @abstractmethod
    def ch_minus(self):
        pass

class TV1(Remote):
    def toggle(self):
        print("TV ON/OFF")
    def ch_plus(self):
        print("tv1 ch plus execute.....!!!")
    def ch_minus(self):
        print("tv1 ch minus execute.....!!!")
class TV2(Remote):
    def toggle(self):
        print("TV ON/OFF")
    def ch_plus(self):
        print("tv2 ch plus execute.....!!!")
    def ch_minus(self):
        print("tv1 ch minus execute.....!!!")
tv=TV1()
tv.toggle()
tv.ch_plus()

tv=TV2()
tv.toggle()
tv.ch_plus()


