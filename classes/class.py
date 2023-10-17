print("Hello World!")

# name:str =88
# print(name)
# (python12) C:\Users\MEMM PC\class01>mypy class.py
# class.py:3: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 1 error in 1 file (checked 1 source file)

name:str ="Masab Bin Zia"
print(name)

name :tuple[str,int,float] = ['pakistan',2121,20.0]
print(name)
print(type(name))
print(id(name))
print([i for i in dir(name) if "__" not in i])