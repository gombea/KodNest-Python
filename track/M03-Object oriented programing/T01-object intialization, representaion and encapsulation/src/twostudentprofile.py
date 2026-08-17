class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course


first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

s1 = StudentProfile(first_id, first_name, first_course)
s2 = StudentProfile(second_id, second_name, second_course)

print("Student 1")
print(f"ID: {s1.student_id}")
print(f"Name: {s1.name}")
print(f"Course: {s1.course}")

print("Student 2")
print(f"ID: {s2.student_id}")
print(f"Name: {s2.name}")
print(f"Course: {s2.course}")