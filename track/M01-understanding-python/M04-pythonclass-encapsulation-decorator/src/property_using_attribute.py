from ast import arguments
class Student:
    def __init__(self,roll,name):
        self.__roll = roll
        self.__name = name
        
    @property
    def roll(self):
        return self.__roll

    @property
    def name(self):
        return self.__name
    
    @roll.setter
    def roll(self,roll):
        self.__roll = roll

    @name.setter
    def name(self,name):
        self.__name = name

s1 = Student(101,"vaishnavi")
print(s1.roll)
print(s1.name)
s1.roll = 200
s1.name = "arun"

print(s1.roll)
print(s1.name)# in this program we are going to use a @property for setter and getter method but we are calling as a attribute