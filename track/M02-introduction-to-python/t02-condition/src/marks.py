marks=int(input())
attendence=int(input())
status=str(input())

if marks>=60 and attendence>=75:
    if status=="yes":
        print("Eligible")
    else:
        print("not eligible")

else:
    print("not eligible")