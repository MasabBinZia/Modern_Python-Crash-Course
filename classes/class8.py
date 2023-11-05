from typing import Dict,Union,Optional


Key = Union[int,str]
Value =Union[int,str,list,dict,tuple,set]


data: Dict[Key, Value] = {
    "fname": "Masab", 
    "name": "Mbz", 
    "lname": "Zia",
    }

print('Before',data)

a:str = data.pop("lname")
print(a)
print('After',data)

b:str = data.get("Pakistan","NA")
print(b)
print('After',data)

a:str = data.setdefault("Pakistan",'Empty value')
print(a)
print('After',data)


from typing import Dict, Union

Key = Union[int, str]
Value = Union[int, str, list, dict, tuple, set]

d1: Dict[Key, Value] = {
    "fname": "Masab", 
    "name": "Mbz", 
    "lname": "Zia",
}

data1:[Key,Value] = {"name":"MasabMBZ",
                     "Age":22,
                     "Height":"6FT"
                     }

d1.update(data1)
print(d1)


import pandas as pd
from typing import Dict, List

Stud_Data: Dict[str, List[any]] = {
    "roll_no": [1, 2, 3, 4],
    "Name": ["Masab", "MBz", "Zia", "Tafi"],
    "Edu": ["MS", "BS", "BBA", "Inter"]
}

df: pd.DataFrame = pd.DataFrame(Stud_Data)

print(df)

alien_0 :Dict [str,any]={
    "x-pos" :0,
    "y-pos" :25,
    "speed": "medium"
}
print(f"Orignal Postion {alien_0["x-pos"]}")

if alien_0["speed"] == 'slow':
    x_increment : int = 1
elif alien_0["speed"] == 'medium':
 x_increment : int = 2
else:
 x_increment : int = 4

alien_0["x-pos"] += x_increment
print(f"Orignal Postion {alien_0["x-pos"]}")

    