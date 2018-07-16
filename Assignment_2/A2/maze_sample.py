import sys
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
    def isGate(self, i, j):
        if i==0 and self.maze[i][j]&1 \
        or i==self.row-1 and  self.maze[i][j]&4 \
        or j==0 and self.maze[i][j]&2 \
        or j==self.col-1 and  self.maze[i][j]&8:
            return True
        else:
            return False
    def getGates(self):
        self.gateCount=0
        self.gates=[]
        for i in range(self.col):
            if self.maze[0][i]&1:
                self.gateCount+=1
                self.gates.append((0,i))
            if self.maze[-1][i]&4:
                self.gateCount+=1
                self.gates.append((self.row-1,i))
        for i in range(self.row):
            if self.maze[i][0]&2:
                self.gateCount+=1
                self.gates.append((i,0))
            if self.maze[i][-1]&8:
                self.gateCount+=1
                self.gates.append((i,self.col-1))
        return
    def deal(self):
        def direcNum(direc):
            count=0
            while direc:
                count+=1
                direc=direc&(direc-1)
            return count
        def goMaze(i,j,direc):
            if marked[i][j]>2:
                return
            if marked[i][j]:
                if (i,j) in route:
                    loops=route.index((i,j))
                    for k in range(loops,len(route)):
                        marked[route[k][0]][route[k][1]]=3
                else:
                    marked[i][j]=3
                return
            marked[i][j]=1
            mmm=self.maze[i][j]
            if direc==mmm:
                return
            if direc==0 and direcNum(mmm)==1:
                return
            route.append((i,j))
            if (len(self.gateOutDirec(i,j))==1 and direc!=0) or (direc==0 and len(self.gateOutDirec(i,j))==2):
                for r,c in route:
                    marked[r][c]+=1
                connectGates.append((i,j))
            if len(self.gateOutDirec(i,j))>2:
                marked[i][j]+=2
            if i>0 and direc!=1 and mmm&1:
                goMaze(i-1,j,4)
            if j>0 and direc!=2 and mmm&2:
                goMaze(i,j-1,8)
            if i<self.row-1 and direc!=4 and mmm&4:
                goMaze(i+1,j,1)
            if j<self.col-1 and direc!=8 and mmm&8:
                goMaze(i,j+1,2)
            route.pop()
        def findRoute(i,j,direc):
            if marked[i][j]!=2:
                return
            else:
                if (len(self.gateOutDirec(i,j))==1 and direc!=0) or (direc==0 and len(self.gateOutDirec(i,j))==2):
                    self.availableRoute.append(route)
                mmm=self.maze[i][j]
                route.append((i,j))
                if i>0 and direc!=1 and mmm&1:
                    findRoute(i-1,j,4)
                if j>0 and direc!=2 and mmm&2:
                    findRoute(i,j-1,8)
                if i<self.row-1 and direc!=4 and mmm&4:
                    findRoute(i+1,j,1)
                if j<self.col-1 and direc!=8 and mmm&8:
                    findRoute(i,j+1,2)
                return
        def findCul_de_sacs(i,j,direc):
            if marked[i][j]!=1:
                return
            else:
                marked[i][j]=-1
                mmm=self.maze[i][j]
                if i>0 and direc!=1 and mmm&1:
                    findCul_de_sacs(i-1,j,4)
                if j>0 and direc!=2 and mmm&2:
                    findCul_de_sacs(i,j-1,8)
                if i<self.row-1 and direc!=4 and mmm&4:
                    findCul_de_sacs(i+1,j,1)
                if j<self.col-1 and direc!=8 and mmm&8:
                    findCul_de_sacs(i,j+1,2)
                return
        self.aeraCount=0
        self.cul_de_sacsCount=0
        self.inaccessible=0
        marked=[[0]*self.col for i in range(self.row)]
        self.availableRoute=[]
        self.getGates()
        for i,j in self.gates:
            if marked[i][j]:
                continue
            self.aeraCount+=1
            route=[]
            connectGates=[]
            goMaze(i,j,0)
            if len(connectGates)==1:
                route=[]
                findRoute(i,j,0)
        for i in range(self.row):
            for j in range(self.col):
                if marked[i][j]==1:
                    self.cul_de_sacsCount+=1
                    findCul_de_sacs(i,j,0)
        for i in range(self.row):
            for j in range(self.col):
                if marked[i][j]==0:
                    self.inaccessible+=1
        self.WallSets()
        return marked
    def WallSets(self):
        self.wallCount=0
        reached=[[0]*(self.col+1) for i in range(self.row+1)]
        def findWall(i,j):
            reached[i][j]=self.wallCount
            if j<self.col and (self.wall[i][j]==1 or self.wall[i][j]==3):
                if self.wall[i][j+1]!=0 and not reached[i][j+1]:
                    findWall(i,j+1)
                if (self.wall[i-1][j+1]==2 or self.wall[i-1][j+1]==3) and not reached[i-1][j+1]:
                    findWall(i-1,j+1)
            if i<self.row and (self.wall[i][j]==2 or self.wall[i][j]==3):
                if self.wall[i+1][j]!=0 and not reached[i+1][j]:
                    findWall(i+1,j)
                if (self.wall[i+1][j-1]==1 or self.wall[i+1][j-1]==3) and not reached[i+1][j-1]:
                    findWall(i+1,j-1)
            if j>0 and (self.wall[i][j-1]==1 or self.wall[i][j-1]==3) and not reached[i][j-1]:
                findWall(i,j-1)
            if i>0 and (self.wall[i-1][j]==2 or self.wall[i-1][j]==3) and not reached[i-1][j]:
                findWall(i-1,j)
            return
        for i in range(self.row+1):
            for j in range(self.col+1):
                if self.wall[i][j]==0 or reached[i][j]:
                    continue
                self.wallCount+=1
                findWall(i,j)
        return
    def getInaccessible(self):
        return self.inaccessible
    def getAeraCount(self):
        return self.aeraCount
    def getCul_de_sacsCount(self):
        return self.cul_de_sacsCount
    def getAvailableRoute(self):
        return self.availableRoute
    def getGateCount(self):
        return self.gateCount
    def getWallSetsCount(self):
        return self.wallCount

    def gateOutDirec(self,i,j):
        direc=[]
        if i==0 and self.maze[i][j]&1:
            direc.append(1)
        if i==self.row-1 and  self.maze[i][j]&4:
            direc.append(4)
        if j==0 and self.maze[i][j]&2:
            direc.append(2)
        if j==self.col-1 and  self.maze[i][j]&8:
            direc.append(8)
        return direc

    def getPaintRoute(self):
        def addRoute(i,j,direct):
            if direct&1 and not paintRoute[i][j+1]&2:
                paintRoute[i][j+1]+=2
            if direct&2 and not paintRoute[i+1][j]&1:
                paintRoute[i+1][j]+=1
            if direct&4 and not paintRoute[i+1][j+1]&2:
                paintRoute[i+1][j+1]+=2
            if direct&8 and not paintRoute[i+1][j+1]&1:
                paintRoute[i+1][j+1]+=1
        paintRoute=[[0]*(self.col+1) for i in range(self.row+1)]
        for route in self.availableRoute:
            for idx in range(len(route)-1):
                i=route[idx][0]
                j=route[idx][1]
                i1=route[idx+1][0]
                j1=route[idx+1][1]
                if i==i1 and j+1==j1:
                    paintRoute[i+1][j+1]+=1
                if i==i1 and j-1==j1:
                    paintRoute[i+1][j]+=1
                if i+1==i1 and j==j1:
                    paintRoute[i+1][j+1]+=2
                if i-1==i1 and j==j1:
                    paintRoute[i][j+1]+=2
            direct=self.gateOutDirec(route[0][0],route[0][1])
            for d in direct:
                addRoute(route[0][0],route[0][1],d)
            direct=self.gateOutDirec(route[-1][0],route[-1][1])
            for d in direct:
                addRoute(route[-1][0],route[-1][1],d)
        return paintRoute


def transformNum(i):
    if i==0:
        return 'no'
    elif i==1:
        return 'a unique'
    else:
        return str(i)
def hasS(i):
    if i<=1:
        return ''
    else:
        return 's'
isPrint=False
fileName=''
for i in range(1,len(sys.argv)):
    if sys.argv[i]=='-print':
        isPrint=True
    elif sys.argv[i]=='--file':
        if i==len(sys.argv)-1:
            print('Incorrect input.')
            exit()
        fileName=sys.argv[i+1]
        i+=1
    elif sys.argv[i-1]!='--file':
        print('Incorrect input.')
        exit()
if fileName=='':
    print('Incorrect input.')
    exit()
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
mark=maze.deal()
route=maze.getAvailableRoute()
if isPrint:
    print('The maze has '+transformNum(maze.getGateCount())+' gate'+hasS(maze.getGateCount())+'.')
    print('The maze has '+transformNum(maze.getWallSetsCount())+' set'+hasS(maze.getWallSetsCount())+' of walls that are all connected.')
    print('The maze has '+transformNum(maze.getInaccessible())+' inaccessible inner point'+hasS(maze.getInaccessible())+'.')
    print('The maze has '+transformNum(maze.getAeraCount())+' accessible area'+hasS(maze.getAeraCount())+'.')
    print('The maze has '+transformNum(maze.getCul_de_sacsCount())+' set'+hasS(maze.getCul_de_sacsCount())+' of accessible cul-de-sacs that are all connected.')
    print('The maze has '+transformNum(len(route))+' entry-exit path'+hasS(len(route))+' with no intersection'+hasS(len(route))+' not to cul-de-sacs.')
fileName=fileName.split('.')[0]+'.tex'
fout=open(fileName,'w')
fout.write('\\documentclass[10pt]{article}\n')
fout.write('\\usepackage{tikz}\n')
fout.write('\\usetikzlibrary{shapes.misc}\n')
fout.write('\\usepackage[margin=0cm]{geometry}\n')
fout.write('\\pagestyle{empty}\n')
fout.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
fout.write('\n')
fout.write('\\begin{document}\n')
fout.write('\n')
fout.write('\\vspace*{\\fill}\n')
fout.write('\\begin{center}\n')
fout.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')
fout.write('% Walls\n')
row=len (wall)-1
col=len(wall[0])-1
for i in range(row+1):
    flag=False
    for j in range(col+1):
        if wall[i][j]==1 or wall[i][j]==3:
            if not flag:
                fout.write('    \\draw ('+str(j)+','+str(i)+')')
                flag=True
        else:
            if flag:
                fout.write(' -- ('+str(j)+','+str(i)+');\n')
                flag=False
for j in range(col+1):
    flag=False
    for i in range(row+1):
        if wall[i][j]==2 or wall[i][j]==3:
            if not flag:
                fout.write('    \\draw ('+str(j)+','+str(i)+')')
                flag=True
        else:
            if flag:
                fout.write(' -- ('+str(j)+','+str(i)+');\n')
                flag=False

fout.write('% Pillars\n')
for i in range(row+1):
    for j in range(col+1):
        if wall[i][j]==0:
            flag=False
            if ((i>0 and (wall[i-1][j]==1 or wall[i-1][j]==0)) or i==0)\
            and ((j>0 and (wall[i][j-1]==2 or wall[i][j-1]==0)) or j==0):
                fout.write('    \\fill[green] ('+str(j)+','+str(i)+')')
                fout.write(' circle(0.2);\n')

fout.write('% Inner points in accessible cul-de-sacs\n')
for i in range(row):
    for j in range(col):
        if mark[i][j]==-1:
            fout.write('    \\node at ('+str(j+0.5)+','+str(i+0.5)+')')
            fout.write(' {};\n')

fout.write('% Entry-exit paths without intersections\n')
paintRoute=maze.getPaintRoute()
for i in range(row+1):
    flag=False
    for j in range(col+1):
        if paintRoute[i][j]==1 or paintRoute[i][j]==3:
            if not flag:
                fout.write('    \\draw[dashed, yellow] ('+str(j-0.5)+','+str(i-0.5)+')')
                flag=True
        else:
            if flag:
                fout.write(' -- ('+str(j-0.5)+','+str(i-0.5)+');\n')
                flag=False
        if j==col and flag:
            fout.write(' -- ('+str(j+0.5)+','+str(i-0.5)+');\n')

for j in range(col+1):
    flag=False
    for i in range(row+1):
        if paintRoute[i][j]==2 or paintRoute[i][j]==3:
            if not flag:
                fout.write('    \\draw[dashed, yellow] ('+str(j-0.5)+','+str(i-0.5)+')')
                flag=True
        else:
            if flag:
                fout.write(' -- ('+str(j-0.5)+','+str(i-0.5)+');\n')
                flag=False
        if i==row and flag:
            fout.write(' -- ('+str(j-0.5)+','+str(i+0.5)+');\n')
fout.write('\\end{tikzpicture}\n')
fout.write('\\end{center}\n')
fout.write('\\vspace*{\\fill}\n')
fout.write('\n')
fout.write('\\end{document}\n')
