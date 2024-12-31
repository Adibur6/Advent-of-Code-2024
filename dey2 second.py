from typing import List, Tuple

l1: List[List[int]] = []

with open('2.txt','r') as file:
    for line in file:
        l1.append(list(int(x) for x in line.split()))

def is_good(l:List[int]) -> bool:
    return all( (l[i]<l[i+1]<l[i]+4) for i in range(len(l) - 1))

def all_good(l:List[int]) -> bool:
    return is_good(l) or any(is_good(l[:x]+l[x+1:]) for x in range(len(l))) 


print(sum([(all_good(sublist) or all_good(sublist[::-1])) for sublist in l1]))