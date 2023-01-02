N,r,c = map(int,input().split())

def divideAndConquer(startNum, lastNum, boardSize, startRow, startCol, r, c):
    if boardSize == 1 and startRow == r and startCol == c:
        return startNum
    
    f = (lastNum - startNum+1)//4 # 4
    
    if startRow <= r < startRow + boardSize//2 and startCol <= c < startCol + boardSize//2: # 1사분면
        return divideAndConquer(startNum, startNum+ f*1 -1, boardSize//2, startRow, startCol, r, c)
        
    elif startRow <= r < startRow + boardSize//2 and startCol + boardSize//2 <= c < startCol + boardSize: # 2사분면
        return divideAndConquer(startNum+f*1, startNum+f*2 -1, boardSize//2, startRow, startCol + boardSize//2, r, c)
        
    elif startRow + boardSize//2 <= r < startRow + boardSize and startCol <= c < startCol + boardSize//2: # 3사분면
        return divideAndConquer(startNum+f*2, startNum+f*3 -1, boardSize//2, startRow + boardSize//2, startCol, r, c)
        
    elif (startRow + boardSize//2) <= r < (startRow + boardSize) and (startCol + boardSize//2) <= c < (startCol + boardSize): # 4사분면
        return divideAndConquer(startNum+ f*3, lastNum, boardSize//2, startRow + boardSize//2, startCol + boardSize//2, r, c)

boardSize = (2**N)
startNum = (2**0)-1
lastNum = (2**N)*(2**N)-1
if N==1:
    if r==0 and c==0 :
        answer = 0
    elif r==0 and c==1 :
        answer = 1
    elif r==1 and c==0 :
        answer = 2
    elif r==1 and c==1 :
        answer = 3
        
else :
    answer = divideAndConquer(startNum,lastNum,boardSize,0,0,r,c)
print(answer)