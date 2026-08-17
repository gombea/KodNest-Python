class StudentProfile:
    def __init__(self, name, experience, skills):
        self.name = name
        self.experience = experience
        self.skills = skills

    def update_experience(self, new_experience):
        self.experience = new_experience

    def add_skill(self, new_skill):
        self.skills.append(new_skill)


name = input().strip()
experience = int(input())
skills = input().split()
new_experience = int(input())
new_skill = input().strip()

s1 = StudentProfile(name, experience, skills)

s1.update_experience(new_experience)
s1.add_skill(new_skill)

print(f"Name: {s1.name}")
print(f"Experience in Years: {s1.experience}")
print(f"Skills: {', '.join(s1.skills)}")