class StudentProfile:
    def __init__(self,student_id,name,course,score):
        self.student_id = student_id
        self.student_name = name
        self.student_course = course
        self.__score = score

    def get_score(self):
        return self.__score

    def update_score(self,new_score):
        if new_score <= 100:
            self.__score = new_score
        else:
            print("invalid score")

    def get_status(self):
        if self.__score >= 60:
            return "Ready"
        else:
            return "Needs Practice"

    def __str__(self):
        return f"name:{self.student_name},student_id:{self.student_id},student_course:{self.student_course},score:{self.__score}"

sid = int(input("Enter student ID: "))
name = input("Enter name: ")
course = input("Enter course: ")
score = int(input("Enter score: "))

# Create the object
student = StudentProfile(sid, name, course, score)

# Use it
print(student)                     # calls __str__ automatically
print("Status:", student.get_status())