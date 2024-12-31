from typing import List
l1: List[int] = []
l2: List[int] = []
with open('1.txt','r') as file:
    for line in file:
        #print(line)
        line = str(line).split()
        #print(line)
        l1.append(int(line[0]))
        l2.append(int(line[1]))
l1.sort()
l2.sort()
ans:int = 0
for i in range(len(l1)):
    ans += abs(l1[i]-l2[i])
print(ans)