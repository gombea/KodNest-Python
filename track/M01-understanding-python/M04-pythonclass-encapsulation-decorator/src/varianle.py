a = 100 #global variable==present outside the class

class Employee:
    companyName = "WIPRO" #class variable==present inside the class,belong to class and outside the method or function
    def __init__(self, id, name):# id and name-->local 
        self.id = id # self.id -->instance variable
        self.name = name # self.name -->instance variable-->which belong to object
     
    def printDetails(self):
        print(self.id)
        print(self.name)
        print(Employee.companyName)




e1 = Employee(11, "Arun")#e1 is a reference variable==holds the address of an object
print(e1.id)
print(e1.name)
print(Employee.companyName)
print()

e1.printDetails()
print()

print("----------------------")
e2 = Employee(12,"Kumar")
print(e2.id)
print(e2.name)
print(Employee.companyName)
print()
e2.printDetails()