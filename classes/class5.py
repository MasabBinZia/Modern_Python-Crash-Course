names: list[str] = ["Masab", "Mbz", "masanz"]
for name in names:
    print(f"name {name.title()}")
    print("WebDev\n")


data_base: list[tuple[str, str]] = [("masab", "123"), ("mbz", "2323")]
input_user: str = input("Enter User Name :")
input_pass: str = input("Enter Password :")

for row in data_base:
    user, password = row
    if input_user == user and input_pass == password:
        print(f"Welcome {user}")
        break
    else:
        print("inValid user OR password")


magicians :list[str] = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank You!")


for n in range(2,21,2):
    print(n)


magicians :list[str] = ['alice', 'david', 'carolina']
for index,name in (enumerate(magicians)):
    print(index,name)


for n in range(1, 11):
    print(f"{2} X {n} = {n*2}")

squares :list[int]=[]
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)


 [i**2 for i in range(1,11)]

digits:list[int]=[1,2,3,4,5,6,7,13]
print(digits)
print(max(digits))
print(min(digits))
print(sum(digits))

my_foods:list[str]= ['Pizza','Falafel','Cake']
friend_foods=my_foods[:]

print(my_foods)
print(friend_foods)

friend_foods[0]="Tikka"

print(my_foods)
print(friend_foods)


name1:tuple[str]= ("A","B","C")
print(name1[0])
print(name1[0:2])




