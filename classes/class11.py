list_a :list[int]=[1,2,3]
list_b =list_a
list_a.append(4)
print("list_b",list_b)

num_a:int=5
num_b=num_a
num_a +=1
print(num_b)
print(num_a)


x =10
print("Before modification",x,id(x))
x+=1
print("After modification",x,id(x))

a:int=5
def abc(num1:int)->None:
    num1=6
    print(f"Num1 Value {num1}")

abc(a)
print(a)

a_1:list[int]=[1,2,3,4,5]
def xyz(num1:list[int])->None:
    num1.append(200)
    print(f"Num1 Value {num1}")

xyz(a_1)
print(a_1) 

a_2:list[int]=[1,2,3,4,5]
def zyx(num1:list[int])->None:
    num1=[7]
    num1.append(200)
    print(f"Num1 Value {num1}")

zyx(a_2)
print(a_2) 


x_1 :int =4
b_1:int =int(4)
print(f'X value is {x_1} & address {id(x_1)}')
print(f'X value is {b_1} & address {id(b_1)}')

b_1=200
print(f'X value is {b_1} & address {id(b_1)}')

a_2:int=int(input("Enter Number 1 "))
b_2:int=int(input("Enter Number 2 "))

print(a_2/b_2)

names:list[str]=["Masab","Mbz","Ilyas"]
indx :int =int(input("Enter index Number"))
print(names[indx])

data:dict[str,str]={
    "name":"Masab",
    "educ":"BS"
}
print(data["fname"])

print("Logic1")
print("Logic2")
try:
    print(5/0)
except(ZeroDivisionError):
    print("ERROR")
print("Logic4")
print("Logic5")


print("Logic1")
print("Logic2")
l_1:list[int]=[1,2,3]
try:
    print(5/2)
    print(l_1[0])
    print(xyz)
except(ZeroDivisionError,IndexError,NameError):
    print("ERROR")
print("Logic4")
print("Logic5")