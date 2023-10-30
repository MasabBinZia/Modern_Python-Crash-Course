from typing import Dict,Union,Optional
import pprint

Key = Union[int,str]
Value =Union[int,str,list,dict,tuple,set]


data: Dict[Key, Value] = {
    "fname": "Masab", 
    "name": "Mbz", 
    "lname": "Zia",
    100:"Pakistan",
    "abc":{1,2,3},
    "xyz":[1,2,3],
    "efg":(1,2,3),
    "zxc":{"a":1,"b":2}
    }

pprint.pprint(data)
print(data["fname"])
print(data["name"])
print(data["lname"])
print(data[100])
print(data["xyz"])

data["name"]= "Masab Bin Zia"
print(data["name"])
print(data.get["name","NA"])

print(data.keys())
print(data.values())
print(data.items())



for v in data.values():
    print(v)

for k,v in data.items():
    print(f"Key:{k}, Value:{v}")

keys :list[str]=['id',"Name","FirstName","Course"]

StdData:dict[keys,Value]={}

print(StdData)
StdData = StdData.fromkeys(keys)
print(StdData)