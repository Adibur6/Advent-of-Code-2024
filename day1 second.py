from typing import List, Dict
l1: List[int] = []
l2: List[int] = []
with open('1.txt','r') as file:
    for line in file:
        line = str(line).split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))

ans:int = 0
counter: Dict[int,int] = {}
for i in l2:
    counter[i] = counter.get(i,0)+1
for i in l1:
    ans += i*counter.get(i,0)
print(ans)