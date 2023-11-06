from typing import Tuple
from typing import Callable
from collections.abc import Iterator


def piaic()->None:
    print("PIAIC")
    print("Python")

piaic()

def addition(num1:int,num2:int)->int:
  print(num1 + num2)

addition(5,10)


def multiply(num1:int,num2:int=0)->int:
  print(num1 * num2)

multiply(5,10)

a = lambda num1,num2 :num1+num2
print(a(7,8))

data:list[int]=[1,2,3,4,5,6,7,8,9,10]
data = list(map(lambda x:x**2, data))
print(data)

data_1:list[int]=[1,2,3,4,5,6,7,8,9,10]
data_1 = list(filter(lambda x:x%2==0, data_1))
print(data_1)


add:Callable[[int,int],int] =lambda x,y: x+y
result:int = add(20,93)
print(result)

def my_range(start:int,end:int,step:int=1):
    for i in range(start,end+1,step):
        yield i

a = my_range(1,10)
print(next(a))
print(next(a))
print(next(a))


def my_range(start:int,end:int,step:int=1)->Iterator[int]:
    for i in range(start,end+1,step):
        yield i

Iterator_Variable :Iterator[int] = my_range(1,10)
print(next(Iterator_Variable))
print(type(Iterator_Variable))

for more in Iterator_Variable:
    print(more)


def abc(*nums):
    print(nums,type(nums))
    total =0 
    for n in nums:
        total+=n
        return total
abc(1,2,3,4,5)


def Add(num1:int,num2:int)->int:
    print(f"Num1 Val {num1} & Num2 Val {num2}")
    return(num1 + num2)

Add(num2=5,num1=10)


def xyz(**kargs):
    print(kargs,type(kargs))

xyz(a=10,b=3,c=5,d=90,name="Masab")


def my_function(a: int, b: int, *abc: Tuple[int, ...], **xyz: dict[str, int]) -> None:
    print(a, b, abc, xyz)

my_function(1, 2, (7, 9, 9, 9), d=30, x=656, y=656)



def greet(*names:Tuple[str,...])->None:
    """
    This Function greets all persons in the names tuple.
    """
    for name in names:
        print("Hello",name)

greet("Masab","Luke","Steve","John","Masab")

def greet(**xyz:dict[str,str])->None:
   print(xyz)
greet(a="Masab",b="Luke",c="Steve",d="John",e="MBz")

def decorator(func:Callable[[],None])->Callable[[],None]:
    def wrapper()->None:
        print("Before Function")
        func()
        print("After Function")
    return wrapper

@decorator
def say_hello()->None:
    print("Hello!")

say_hello()

def decorator1(func:Callable[[int],None])->Callable[[int],None]:
    def wrapper1(num1:int)->None:
        print("Before Function")
        func(num1)
        print("After Function")
    return wrapper1

@decorator1
def say_hello1(num1:int):
    print(num1)

say_hello1(100)

def factorial(x: int) -> int:
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
        #       5*4*3*2*1

num = 5
print("The factorial of", num, "is", factorial(num))