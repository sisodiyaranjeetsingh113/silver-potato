'''
constructor
'''
class Animal:
    def __init__(self):
        print("Kon h bhai...!")
    def run(self):
        print("Run function called......!!!")
        print(self.name)   
        print(self.color)
    
    def eat(self):
        print("Eat function called......!!!")
        print(self.name)   
        print(self.color)

dog=Animal() 
dog.name="dabar"
dog.color="white"
dog.run()     #object is user define datatype
dog.eat()

cat=Animal()
cat.name="welly"
cat.color="black"
cat.run()     #object is user define datatype
cat.eat()


