

class Maze():
    def __init__(self,  _walls):
        self.wall=_walls
        self.row=len (wall) -1
        self.col=len(wall[0])-1
        self.maze=[]
        for i in range(self.row):
            tempRow=[]
            for j in range(self.col):
                cell=3-wall[i][j]
                if self.wall[i+1][j]==2 or self.wall[i+1][j]==0:
                    cell+=4
                if self.wall[i][j+1]==1 or self.wall[i][j+1]==0:
                    cell+=8
                tempRow.append(cell)
            self.maze.append(tempRow)
        for x in self.maze:
            for y in x:
                print('{:2}'.format(y),end=' ')
            print()
import sys
fileName=input('input filename')
try:
    fin=open(fileName,'r')
    data=fin.readlines()
except IOError:
    print('Incorrect input.')
    exit()
fin.close()
wall=[]
for i in data:
    line=[]
    for j in i:
        if j!=' ' and j!='\n':
            if not 0<=int(j)<=3:
                print('Incorrect input.')
                exit()
            line.append(int(j))
    if line!=[]:
        wall.append(line)
maze=Maze(wall)
