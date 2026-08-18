class StudentProfile:
    def __intit__(self,student_name,student_id,student_course,student_email,student_skills)
    self.student_name = student_name
    self.student_id = student_id
    self.student_course = student_course
    self.student_email = student_email
    self.student_skills = student_skills


student_name = input("enter your name")
student_id = int(input("Enter student ID"))
student_course = input("Course:")
student_email = input("Enter email")
student_skills = list(map(int,input("Enter skills").split()))
    
student1 = StudentProfile(student_name,student_id,student_course,student_email,student_skills)
print(student1.student_name)
print(student1.student_id)
print(student1.student_course)
print(student1.student_email)
print(student1.student_skills)
