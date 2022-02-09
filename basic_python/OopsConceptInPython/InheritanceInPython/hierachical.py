class Animal:
    def __init__(self,name):
        self.name=name
    def run(self):
        print(self.name," is running")
    def eat(self):
        print(self.name,"is eating")
     def sleep(self):
        print(self.name," sleeping")
class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name) 
        self.color=color
    def getName(self):
      print("My dog name is",self.name)
    def getColor(self):
     print(self.name," color is",self.color)
class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def getName(self):
      print("My cat name is",self.name)
    def getColor(self):
     print(self.name," color is",self.color)
dog=Dog("tuffy","red")
dog.getName()
dog.getColor()
dog.run()
dog.eat()
dog.sleep()
cat=Cat("welly","black")
cat.getName()
cat.getColor()
cat.run()
cat.eat()
cat.sleep()
