from typing import List, Set, Tuple
lines:List[str]=[]

with open('4.txt','r') as file:
    for line in file:
        lines.append(line.strip())
def getDirections() -> Set[Tuple[int,int]]:
    
    moves: Set[Tuple[int,int]] = set([(-1,-1),(1,-1),(-1,1),(1,1)])
    
    return moves

def is_valid(index1,index2,move,x,y) -> bool:
    #print(index1,index2,move,x,y)
    if index1+move[0]<x and index1+move[0]>=0:
        if index2+move[1]<y and index2+move[1]>=0:
            return True
        return False
    return False
def getWord(index1,index2,lines,move):
    start1= index1
    finish1= index1+move[0]
    start2 =index2
    finish2 =index2 +move[1]
    reverse1 = False
    reverse2 = False
    if start1> finish1:
        start1,finish1 = finish1, start1
        reverse1 = True
    if start2> finish2:
        start2,finish2 = finish2, start2
        reverse2 = True
    range1 = list(range(start1,finish1+1))
    range2 = list(range(start2,finish2+1))
    if reverse1:
        range1 = range1[::-1]
    if reverse2:
        range2 = range2[::-1]
    if move[0]==0:
        while len(range1)!= len(range2):
            range1.append(range1[-1]);
    if move[1]==0:
        while len(range1)!= len(range2):
            range2.append(range2[-1]);
    
    word:str = ''
    #print(list(zip(range1,range2)))
    for x,y in zip(range1,range2):
        word += lines[x][y]

    return word
        

def countWord(lines:List[str]):
    moves= getDirections()
    cnt:int = 0
    for index1 in range(len(lines)):
        for index2 in range(len(lines[0])):
            foundWords: List[str]= [] 
            for move in moves:
                if is_valid(index1,index2,move,len(lines),len(lines[0])):
                    foundWords.append( getWord(index1,index2,lines,move))
            print(foundWords)
            expected = ['AM','AM','AS','AS']
            okay = 4
            while okay >0:
                if foundWords==expected:
                    cnt += 1
                    break
                expected = expected[-1:] + expected[:-1]
                okay -= 1
                

    return cnt
print(lines)
print(countWord(lines))