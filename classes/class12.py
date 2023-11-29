# class StudentAgeError(Exception):
#     pass


# class StudentCard:
#     def __init__(self, roll_no: int, name: str, age: int) -> None:
#         if age < 18 or age > 70:
#             raise StudentAgeError("You're not eligible for this program")
#         self.roll_no = roll_no
#         self.name = name
#         self.age = age


# student1 = StudentCard(1, "MBZ", 22)
# print(student1.name, student1.age, student1.roll_no)

# from typing import TextIO
# data :TextIO = open("./abc.txt")
# print(data.read())

# data.close()

# with open("./abc.txt") as file:
#     print(file.readline(),end="")


# with open("./abc.txt") as file:
#     print(file.readlines())

# with open("./abc.txt","r+") as file:
#     print(file.read())

#     file.write("We love u")
#     file.seek(0)
#     print("After",file.read())

with open("./abc.txt" ,'w') as file:
    file.write("Pakiatan")

with open("./abc.txt" ,'a') as file:
    file.write("Pakiatan")


with open("./abc.txt" ,'x') as file:
    file.write("Pakiatan")