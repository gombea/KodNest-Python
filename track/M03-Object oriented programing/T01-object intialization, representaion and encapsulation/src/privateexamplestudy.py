class Student:
    def setter(self,roll,name,age,marks):
        self.__roll = roll
        self.__name = name
        self.__age = age
        self.__marks = marks

    def study(self):
        print(self.name,"is studying")


    def get_roll(self,__roll):
        return self.__roll


    def get_name(self,__name):
        return self.__name

    def get_age(self,__age):
        return self.__age

    def get_score(self,__marks):
        return self.__marks

    

s1 = Student(int(input()), input(),int(input()),int(input()))
print(s1.roll)
print(s1.name)
print(s1.age)
print(s1.marks)
s1.study()

s2 = Student(int(input()), input(),int(input()),int(input()))
print(s2.roll)
print(s2.name)
print(s2.age)
print(s2.marks)
s2.study()



 



