import subprocess
from importlib import _bootstrap_external
class Student:
    def __init__(self, roll,name):
        if roll > 0:
            self.__roll = roll
        else:
            self.__roll = None
            print("enter correct roll no") 
        self.__name = name
    @property
    def roll(self):
        return self.__roll
    @property
    def name(self):
        return self.__name

    

    
s1 = Student(101,"vaishnavi")
print(s1.roll)
print(s1.name)