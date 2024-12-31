import re
from typing import List
input:str 
with open('3.txt','r') as file:
    input = str(file.read())
p1 :str = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
p2 :str = r'do\(\)'
p3 :str = r'don\'t\(\)'
l = re.findall(f'{p1}|{p2}|{p3}',input)
enable:bool = True
ans :int = 0
for instruction in l:
    if re.search(p2,instruction):
        enable = True
    elif re.search(p3,instruction):
        enable = False
    elif enable:
        x,y = re.findall('[0-9]+',instruction)
        
        ans += int(x) * int(y)
print(ans)