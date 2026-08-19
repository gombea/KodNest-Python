class Student:
    def __inint__(self,roll,name,age,marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks

    def study(self):
        print(self.name,"is studying")


    

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



 



