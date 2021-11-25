entry = input().split(' ')

rowCount = int(entry[0])
colCount = int(entry[1])

table = [[0 for x in range(colCount)] for y in range(rowCount)] 

def printTable():
    for row in table:
        for col in row:
            print(col, end=' ')
        print('')


bombCount = int(input())

for bomb in range(bombCount):
    bombCoordinate = input().split(' ')


    table[int(bombCoordinate[0]) - 1][ int(bombCoordinate[1]) - 1] = '*'

for rowIndex, row in enumerate(table):
    for colIndex, col in enumerate(row):


        if col != '*':
            nearBombCount = 0

            if rowIndex == 0 and colIndex == 0: 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 

            elif rowIndex == 0 and colIndex != 0 and colIndex != colCount-1: 
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                    
            elif colIndex == 0 and rowIndex != 0 and rowIndex != rowCount-1:
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 

            elif rowIndex == 0 and colIndex == colCount-1:
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 

            elif colIndex == 0 and rowIndex == rowCount-1: 
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 

            elif rowIndex == rowCount-1 and colIndex != colCount-1:
                if table[rowIndex-1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 

            elif colIndex == colCount-1 and rowIndex != rowCount-1: 
                if table[rowIndex-1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 

            elif rowIndex == rowCount-1 and colIndex == colCount-1: 
                if table[rowIndex-1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 

            else:
                if table[rowIndex-1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex-1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex+1] == '*':
                    nearBombCount = nearBombCount + 1 
                if table[rowIndex+1][colIndex-1] == '*':
                    nearBombCount = nearBombCount + 1 

            table[rowIndex][colIndex] = nearBombCount

printTable()

