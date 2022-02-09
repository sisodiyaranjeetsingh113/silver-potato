class EmployeeIDClass:
    __companyName__="PythonMate"
    def __init__(self,Id_Number):
        self.Id_Number=Id_Number
    def get_id_number(self):
        return self.Id_Number
    

class EmployeeNAMEClass(EmployeeIDClass):
    def __init__(self,Id_Number,Name):
        self.Name=Name
        super().__init__(Id_Number)
    def get_name(self):
        return self.Name
class EmployeeSALARYClass(EmployeeNAMEClass):
    def __init__(self,Id_Number,Name,Salary):
        self.Salary=Salary
        super().__init__(Id_Number,Name)
    def get_salary(self):
        return self.Salary

esc=EmployeeSALARYClass("100","Ranjeet","15000")
print(esc.get_id_number())
print(esc.get_name())
print(esc.get_salary())

print(esc.__companyName__)
print(esc.__class__.__companyName__)
