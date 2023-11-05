l1 : list[int]=[1,2,3,4,5,6]
for n in l1:
    print(f"Num : {n}")

l2 : tuple[int]={1,2,3,4,5,6}
for n1 in l2:
    print(f"Num : {n1}")

l3 :str = "Pakistan"
for c in l3:
    print(f"Chracter : {c}")


    
l4 :dict[str,str] = {"Name":"masab","lName":"MBZ"}
for N in l4:
    print(f"Key: {N} and Val : {l4[N]}")


        
l5 :list[set[int]] = list({1,5,6,8,7,9})
for L in l5:
    print(f"Val: {L}")


name : str = input("Give Your Name :")
print(type(name))
print(f"HI! {name}")

import sys 
print("line1")
print("line1")

print(sys.argv)



flag : bool=True
cNum  :int = 1

while flag:
    print("Pakistan")
    cNum +=1
    if cNum == 10:
        break



list_1: list[int] = [100, 200, 300]
index: int = 0

while index < len(list_1):
    print(f"Current index is: {index}  val: {list_1[index]}")
    index += 1

DbData :list[dict[str,str]]=[]
flag1 : bool = True

while flag1:
    print("Write quit to stop this program")
    user_name: str = input("Your Name ? :")
    user_edu :str =input("Your Last Education ? :")
    if user_name  in ['quit','exit'] or user_edu  in ['quit','exit'] :
        flag1:False
        break
    DbData.append({"name":user_name,
                   "education":user_edu
                   })
    print(DbData)

for o in range (1,11):
    print(o)
    if o == 5:
        break


    
for j in range (1,11):
    print(f"2 X {j}={j*2}")
   
for i in range (1,11):
    if i == 5:
        continue
    print(i)


for M in range (1,1000):
    pass



prompt = """If you share your name, we can personalize the messages you see.\
What is your first name? """


name = input(prompt)
print(f"\nHello, {name}!")



age:int = int(input("How old are you? "))
age >= 18
print(age)

data2 : list[int] = [1,3,5,6,3,15,18]

even =[i  for i in data2 if i%2==0]
print(even)


current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 != 0:
        continue
    print(current_number)


prompt1 = "\nTell me something, and I will repeat it back to you:"
prompt1 += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt1)
    print(message)


prompt2:str = "\nTell me something, and I will repeat it back to you:"
prompt2 += "\nEnter 'quit' to end the program. "

active = True 

while active:
    message = input(prompt2)
    if message == 'quit':
        active = False
    else:
        print(message)



unconfirmed_users : list[str] = ['alice', 'brian', 'candace']
confirmed_users : list[str] = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

a1 = 10
while a1:
    print("abc")
    break


data_3 : list[int] = [1,2,3]
while data_3:
    n : int = data_3.pop()
    print(n)


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)