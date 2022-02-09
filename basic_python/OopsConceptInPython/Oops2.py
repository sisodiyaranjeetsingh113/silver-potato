'''
constructor
1. ==> it is same like as fuction...
2. ==>never return any value..
3. ==>define using magic function __init__()
4. ==>no need to call constructor...
5. ==>bcz  when we creating object of class that time automatically constructor invoke
'''
class Animal:
    def __init__(self,name,color):
        print("Kon h bhai...!")
        self.name=name
        self.color=color
    def run(self):
        print("Run function called......!!!")
        print(self.name)   
        print(self.color)
    
    def eat(self):
        print("Eat function called......!!!")
        print(self.name)   
        print(self.color)

dog=Animal("dabar","white")

dog.run()     #object is user define datatype
dog.eat()

cat=Animal("welly","pink")

cat.run()     #object is user define datatype
cat.eat()

