from typing import Union, Optional

if True:
    print("masab")
else:
    print("mbz")


if False:
    print("masab")
else:
    print("mbz")

print("masab") if False else print("mbz")
print("masab") if True else print("mbz")

# one will run block
if False:
    print("True_block")
elif False:
    print("elif Logic1")
elif True:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("Final else block")

print("pakistan")


if False:
    print("True_block")
elif False:
    print("elif Logic1")
elif False:
    print("elif logic2")
elif False:
    print("elif logic3")
else:
    print("Final else block")

print("pakistan")



per: Union[int, float] = float(input("Enter Your Percentage"))
# per:int | float =88
grade: Union[str, None] = None
# grade:Optional[str]=None

if per >= 80:
    grade = "A"
elif per >= 70:
    grade = "B"
elif per >= 60:
    grade = "B"
elif per >= 50:
    grade = "C"
elif per >= 40:
    grade = "D"
elif per >= 33:
    grade = "E"
else:
    grade = "Fail"

print(f"Your Percentage is {per} & your grade is {grade}")


PerType = Union[int, float]
percentages: list[PerType] = [88, 99.2, 70.5, 56.3, 30]
roll_no:list[int]=list(range(len(percentages)))

grades: list[str] = []

for Stud_percentage in percentages:
    grade: str = ""
    if Stud_percentage >= 80:
        grade = "A+"
    elif Stud_percentage >= 70:
        grade = "A"
    elif Stud_percentage >= 60:
        grade = "B"
    elif Stud_percentage >= 50:
        grade = "C"
    elif Stud_percentage >= 40:
        grade = "D"
    elif Stud_percentage >= 33:
        grade = "E"
    else:
        grade = "Fail"
    grades.append(grade)


print(percentages)
print(grades)
print(list(zip(roll_no,percentages,grades)))


cars : list[str] =["Lambi",'audi','bmw','subaru','toyota']
for car in cars:
    if car != 'Lambi':
        print(car.upper())
    else:
        print(car.title())


user_name:str =input("Enter username :")
password:str =input("Enter pass : ")

if user_name == "mbz" and password == 'mbz':
    print('sent Otp ')
    otp : str = input("pls give Otp :")
    if otp == '123':
        print(f"Welcome {user_name}")
else:
    print('invalud user or password')
