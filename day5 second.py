from typing import Set, Tuple, List
ordering: Set[Tuple[int,int]] = set()
sequences: List[List[int]] = []

with open('5.txt','r') as file:
    for line in file:
        line = line.strip()
        if '|' in line:
            ordering.add(tuple(map(int,line.split('|'))))
        if ',' in line:
            sequences.append(list(map(int,line.split(','))))

ans :int = 0
badSequences:List[List[int]] = []
for sequence in sequences:
    okay:bool = True

    for i in range(len(sequence)):
        for j in range(i+1,len(sequence)):
            if (sequence[j],sequence[i]) in ordering:
                okay = False
    if not okay:
        badSequences.append(sequence)
print(badSequences)
for sequence in badSequences:
    okay = True
    while okay:
        okay = False
        for i in range(len(sequence)):
            for j in range(i+1,len(sequence)):
                if (sequence[j],sequence[i]) in ordering:
                    sequence[j],sequence[i] = sequence[i],sequence[j]
                    okay = True
    ans += sequence[len(sequence)//2]
    print(sequence)
print(ans)
        