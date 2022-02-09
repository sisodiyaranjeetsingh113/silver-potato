class India:
    __x=10
    def capital(self):
        print("capital of india")

class Usa:
    def capital(self):
        print("capital of usa")

obj_i=India()
obj_u=Usa()

for country in(obj_i,obj_u):
    country.capital()