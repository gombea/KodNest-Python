skills=[]

for i in range(5):
    skill=input()
    skills.append(skill)

skill_record = tuple(skills)

first = skill_record[3:]
last = skill_record[:3]
alternative = skill_record[::2]
reverse = skill_record[::-1]

print("")

