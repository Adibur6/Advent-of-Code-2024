import re
from typing import List
input:str 
with open('3.txt','r') as file:
    input = str(file.read())
l = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)',input)
ans:int = 0
for x,y in l:
    ans += int(x)*int(y)
print(ans)