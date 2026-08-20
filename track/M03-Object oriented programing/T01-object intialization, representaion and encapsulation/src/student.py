class Student:
    def __init__(self, roll,name):
        if roll > 0:
            self.__roll = roll
        else:
            self.__roll = None
            print("enter correct roll no") 
        self.__name = name

    

    def getRoll(self):
        return self.__roll

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

s1 = Student(-101,"vaishnavi")
print(s1.getRoll())
print(s1.getName())