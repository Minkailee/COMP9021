import sys
from copy import deepcopy
class Point():
    def __init__(self,value):
        self.value=value
        if self.value&1:
            self.up=True
        else:
            self.up=False
        if self.value&2:
            self.left=True
        else:
            self.left=False
        if self.value&4:
            self.down=True
        else:
            self.down=False
        if self.value&8:
            self.right=True
        else:
            self.right=False
class Maze():
    def __init__(self,wall):
        self.way=[]
        self.maze=[]
        self.row=len (wall) -1
        self.col=len(wall[0])-1
        for i in range(self.row):
            line=[]
            for j in range(self.col):
                value=3-wall[i][j]
                if wall[i+1][j]==2 or wall[i+1][j]==0:
                    value+=4
                if wall[i][j+1]==1 or wall[i][j+1]==0:
                    value+=8
                point=Point(value)
                line.append(point)
            self.maze.append(line)
        self.gates=self.getGates()
    def isGate(self, i, j):
        if i==0 and self.maze[i][j].up \
        or i==self.row-1 and  self.maze[i][j].down \
        or j==0 and self.maze[i][j].left \
        or j==self.col-1 and  self.maze[i][j].right:
            return True
        else:
            return False
    def getGates(self):
        self.gateCount=0
        self.gates=[]
        for i in range(self.col):
            if self.maze[0][i].up:
                self.gateCount+=1
                self.gates.append((0,i))
            if self.maze[-1][i].down:
                self.gateCount+=1
                self.gates.append((self.row-1,i))
        for i in range(self.row):
            if self.maze[i][0].left:
                self.gateCount+=1
                self.gates.append((i,0))
            if self.maze[i][-1].right:
                self.gateCount+=1
                self.gates.append((i,self.col-1))
        return self.gates
    def ways(self):
        ways=[]
        for i in range(self.row):
            eachl=[]
            for j in range(self.col):
                count=0
                if self.maze[i][j].up:
                    count+=1
                if self.maze[i][j].down:
                    count+=1
                if self.maze[i][j].right:
                    count+=1
                if self.maze[i][j].left:
                    count+=1
                eachl.append(count)
            ways.append(eachl)
        return ways 
        
        
                
            
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
#fileName=input('fileName:')
try:
    f=open(fileName,'r')
    data=f.readlines()
except IOError:
    print('Incorrect input.')
    exit()
f.close()
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
row=len (wall)-1
col=len(wall[0])-1
for i in wall:
    if len(i)!=col+1:
        print('Incorrect input.')
        exit()
if row+1>41 or col+1>31:
    print('Incorrect input.')
    exit()
for i in range(len(wall[0])):
    if wall[-1][i]==2 or wall[-1][i]==3:
        print('Incorrect input.')
        exit()
for i in range(len(wall)):
    if wall[i][-1]==1 or wall[i][-1]==3:
        print('Incorrect input.')
        exit()
maze=Maze(wall)
maze1=deepcopy(maze)
ways=maze.ways()
def transNum(i):
    if i==0:
        return 'no'
    elif i==1:
        return 'a unique'
    else:
        return str(i)
def getS(i):
    if i<=1:
        return ''
    else:
        return 's'
def scan(ways):
    for i in range(maze.row):
        for j in range(maze.col):
            if ways[i][j]==1:
                ways[i][j]=-1
            if ways[i][j]==-1 and maze1.maze[i][j].up:
                if i==0:
                    continue
                else:
                    ways[i-1][j]-=1
                    maze1.maze[i][j].up=False
                    maze1.maze[i-1][j].down=False
            if ways[i][j]==-1 and maze1.maze[i][j].down:
                if i==maze.row-1:
                    continue
                else:
                    ways[i+1][j]-=1
                    maze1.maze[i][j].down=False
                    maze1.maze[i+1][j].up=False
            if ways[i][j]==-1 and maze1.maze[i][j].right:
                if j==maze.col-1:
                    continue
                else:
                    ways[i][j+1]-=1
                    maze1.maze[i][j].right=False
                    maze1.maze[i][j+1].left=False
            if ways[i][j]==-1 and maze1.maze[i][j].left:
                if j==0:
                    continue
                else:
                    ways[i][j-1]-=1
                    maze1.maze[i][j].left=False
                    maze1.maze[i][j-1].right=False
    for i in range(maze.row):
        for j in range(maze.col):
            if ways[i][j]==1:
                scan(ways)
    return ways
maze.way=scan(ways)
maze1=deepcopy(maze)
allroute=[]
route=[]    
def explore_allroute():
    global route
    for i in range(maze.row):
        for j in range(maze.col):
            if ((i==0 and j==0) and maze.way[i][j]==2 and
                (maze.maze[i][j].up==True and maze.maze[i][j].left==True))\
               or ((i==0 and j==maze.col-1) and maze.way[i][j]==2 and \
               (maze.maze[i][j].up==True and maze.maze[i][j].right==True))\
               or ((i==maze.row-1 and j==0) and maze.way[i][j]==2 and \
               (maze.maze[i][j].down==True and maze.maze[i][j].left==True))\
               or ((i==maze.row-1 and j==maze.col-1) and maze.way[i][j]==2 and \
               (maze.maze[i][j].down==True and maze.maze[i][j].right==True)):
                allroute.append([(i,j)])
            if maze.col==1:
                if (maze1.isGate(i,j) \
                   and maze1.maze[i][j].right==True \
                   and maze1.maze[i][j].left==True\
                   and maze1.maze[i][j].up==False \
                   and maze1.maze[i][j].down==False):
                    allroute.append([(i,j)])
            if maze.row==1:
                if (maze1.isGate(i,j) \
                    and maze1.maze[i][j].right==False \
                   and maze1.maze[i][j].left==False\
                   and maze1.maze[i][j].up==True \
                   and maze1.maze[i][j].down==True):
                    allroute.append([(i,j)])
            else:
                if maze1.isGate(i,j):
                    route=[]
                    route.append((i,j))
                    #print(i,j,'start')
                    explore_route(i,j)
def explore_route(i,j):
    global route
    if maze1.way[i][j]!=2:
        #print('back')
        route=[]
        return
    if maze1.way[i][j]==2:
        if maze1.maze[i][j].up==True and (i-1>=0 and i-1<maze.row and j>=0 and j<maze.col) and maze1.way[i-1][j]==2:
            maze1.maze[i-1][j].down=False
            if maze1.isGate(i-1,j):
                route.append((i-1,j))
                allroute.append(route)
                route=[]
                #maze1.maze[i-1][j].up=False
                #print(i-1,j,'end')
            else:
                route.append((i-1,j))
                #print(i-1,j,'u')
                explore_route(i-1,j)
                      
        if maze1.maze[i][j].down==True and (i+1>=0 and i+1<maze.row and j>=0 and j<maze.col) and maze1.way[i+1][j]==2:
            maze1.maze[i+1][j].up=False
            if maze1.isGate(i+1,j):
                route.append((i+1,j))
                allroute.append(route)
                route=[]
                #maze1.maze[i+1][j].down=False
                #print(i+1,j,'end')
            else:
                route.append((i+1,j))
                #print(i+1,j,'d')
                explore_route(i+1,j)
                
        if maze1.maze[i][j].left==True and (i>=0 and i<maze.row and j-1>=0 and j-1 < maze.col) and maze1.way[i][j-1]==2:
            maze1.maze[i][j-1].right=False
            if maze1.isGate(i,j-1):
                route.append((i,j-1))
                allroute.append(route)
                route=[]
                #maze1.maze[i][j-1].left=False
                #print(i,j-1,'end')
            else:
                route.append((i,j-1))
                #print(i,j-1,'l')
                explore_route(i,j-1)
                
        if maze1.maze[i][j].right==True and (i>=0 and i < maze.row and j+1>=0 and j+1<maze.col) and maze1.way[i][j+1]==2:
            maze1.maze[i][j+1].left=False
            if maze1.isGate(i,j+1):
                route.append((i,j+1))
                allroute.append(route)
                route=[]
                #maze1.maze[i][j+1].right=False
                #print(i,j+1,'end')
            else:
                route.append((i,j+1))
                #print(i,j+1,'r')
                explore_route(i,j+1)               
explore_allroute()
maze2=deepcopy(maze)
ways1=maze2.ways()
areaNum=0
def explore_inaccp_accarea():
    global areaNum
    for i in range(maze.row):
        for j in range(maze.col):
            if maze2.isGate(i,j):
                areaNum+=1
                ways1[i][j]=-1
                #print(i,j,'s')
                explore(i,j)
                
def explore(i,j):
    if ways1[i][j]==1:
        #print(i,j,'b')
        ways1[i][j]=-1
        return
    if maze2.maze[i][j].up==True and (i-1>=0 and i-1<maze.row and j>=0 and j<maze.col):
        maze2.maze[i-1][j].down=False
        if maze2.isGate(i-1,j):
            ways1[i][j]=-1
            ways1[i-1][j]=-1
            if i-1==0:
                maze2.maze[i-1][j].up=False
            if j==0:
                maze2.maze[i-1][j].left=False
            if j==maze.col-1:
                maze2.maze[i-1][j].right=False
            #print(i-1,j,'-')
            explore(i-1,j)        
        elif ways1[i-1][j]==-1:
            ways1[i][j]=-1
            ways1[i-1][j]=1            
            explore(i-1,j)            
        else:
            ways1[i][j]=-1
            #print(i,j,'u')
            explore(i-1,j)
    if maze2.maze[i][j].down==True and (i+1>=0 and i+1<maze.row and j>=0 and j<maze.col):
        maze2.maze[i+1][j].up=False
        if maze2.isGate(i+1,j):
            ways1[i][j]=-1
            ways1[i+1][j]=-1
            if i+1==maze.row-1:
                maze2.maze[i+1][j].down=False
            if j==0:
                maze2.maze[i+1][j].left=False
            if j==maze.col-1:
                maze2.maze[i+1][j].right=False
            #print(i+1,j,'-')
            explore(i+1,j)            
        elif ways1[i+1][j]==-1:
            ways1[i][j]=-1
            ways1[i+1][j]=1            
            explore(i+1,j)            
        else:
            ways1[i][j]=-1
            #print(i,j,'d')
            explore(i+1,j)
    if maze2.maze[i][j].right==True and (i>=0 and i < maze.row and j+1>=0 and j+1<maze.col):
        maze2.maze[i][j+1].left=False
        if maze2.isGate(i,j+1):
            ways1[i][j]=-1
            ways1[i][j+1]=-1
            if j+1==maze.col-1:
                maze2.maze[i][j+1].right=False
            if i==0:
                maze2.maze[i][j+1].up=False
            if i==maze.row-1:
                maze2.maze[i][j+1].down=False
            #print(i,j+1,'-')
            explore(i,j+1)     
        elif ways1[i][j+1]==-1:
            ways1[i][j]=-1
            #print(i,j)
            ways1[i][j+1]=1
            explore(i,j+1)
        else:
            ways1[i][j]=-1
            #print(i,j,'r')
            explore(i,j+1)
    if maze2.maze[i][j].left==True and (i>=0 and i<maze.row and j-1>=0 and j-1<maze.col):
        maze2.maze[i][j-1].right=False
        if maze2.isGate(i,j-1):
            ways1[i][j]=-1
            ways1[i][j-1]=-1
            if j-1==0:
                maze2.maze[i][j-1].left=False
            if i==0:
                maze2.maze[i][j-1].up=False
            if i==maze.row-1:
                maze2.maze[i][j-1].down=False
            #print(i,j-1,'-')
            explore(i,j-1)           
        elif ways1[i][j-1]==-1:
            ways1[i][j]=-1
            #print(i,j)
            ways1[i][j-1]=1            
            explore(i,j-1)
        else:
            ways1[i][j]=-1
            #print(i,j,'l')
            explore(i,j-1)
explore_inaccp_accarea()
inaccessible=[]
for i in range(len(ways1)):
    for j in range(len(ways1[0])):
        if ways1[i][j]!=-1:
            inaccessible.append((i,j))
inaccNum=len(inaccessible)
#print(Numinacc)
#print(acc_areas)
maze3=deepcopy(maze)
ways2=maze3.ways()
scaned=maze3.way
for x in inaccessible:
        scaned[x[0]][x[1]]=0
marked=deepcopy(scaned)
for x in allroute:
    for y in x:
        marked[y[0]][y[1]]=5
maze4=deepcopy(maze)
for i in range(maze.row):
    for j in range(maze.col):
        if marked[i][j]==5:
            if i!=0 and maze4.maze[i][j].up==True and marked[i-1][j]==-1:
                maze4.maze[i][j].up=False
            if j!=0 and maze4.maze[i][j].left==True and marked[i][j-1]==-1:
                maze4.maze[i][j].left=False
            if i!=maze.row-1 and maze4.maze[i][j].down==True and marked[i+1][j]==-1:
                maze4.maze[i][j].down=False
            if j!=maze.col-1 and maze4.maze[i][j].right==True and marked[i][j+1]==-1:
                maze4.maze[i][j].right=False

#for x in marked:
    #for y in x:
        #print('{:3}'.format(y),end='')
    #print()
culNum=0
def cul_de_sacs():
    global culNum
    for i in range(len(ways2)):
        for j in range(len(ways2[0])):
            if scaned[i][j]==-1:
                culNum+=1
                #print(i,j)
                find_cul_de_sacs(i,j)
def find_cul_de_sacs(i,j):
    if maze3.isGate(i,j) and ways2[i][j]==1:
        scaned[i][j]=-2
        pass
    if scaned[i][j]!=-1:
        #print('b')
        return
    if maze3.maze[i][j].up==True and (i-1>=0 and i-1<maze.row and j>=0 and j<maze.col):
        maze3.maze[i-1][j].down=False
        scaned[i][j]=-2
        #print('u')
        if ways2[i-1][j]==1:
            scaned[i-1][j]=-2
        find_cul_de_sacs(i-1,j)
    if maze3.maze[i][j].down==True and (i+1>=0 and i+1<maze.row and j>=0 and j<maze.col):
        maze3.maze[i+1][j].up=False
        scaned[i][j]=-2
        #print('d')
        if ways2[i+1][j]==1:
            scaned[i+1][j]=-2
        find_cul_de_sacs(i+1,j)
    if maze3.maze[i][j].right==True and (i>=0 and i < maze.row and j+1>=0 and j+1<maze.col):
        maze3.maze[i][j+1].left=False
        scaned[i][j]=-2
        #print('r')
        if ways2[i][j+1]==1:
            scaned[i][j+1]=-2
        find_cul_de_sacs(i,j+1)
    if maze3.maze[i][j].left==True and (i>=0 and i<maze.row and j-1>=0 and j-1<maze.col):
        maze3.maze[i][j-1].right=False
        scaned[i][j]=-2
        #print('l')
        if ways2[i][j-1]==1:
            scaned[i][j-1]=-2
        find_cul_de_sacs(i,j-1)
cul_de_sacs()
#print(culNum)
wallNum=0
ways3=deepcopy(wall)
ways4=deepcopy(wall)
def wallsests():
    global wallNum
    for i in range(len(ways3)):
        for j in range(len(ways3[0])):
            if ways4[i][j]!=0:
                wallNum+=1
                #print(i,j,'s')
                find_walls(i,j)
                ways4[i][j]=0
def find_walls(i,j):
    if ways4[i][j]==0:
        #print(i,j,'b')
        return
    if ((i>=0 and i+1<=maze.row and j>=0 and j<=maze.col)\
       and ((ways3[i][j]==2 and ways3[i+1][j]!=0)\
           or (ways3[i][j]==3 and ways3[i+1][j]!=0))): 
               ways4[i][j]=0
               #print(i,j,'d')
               find_walls(i+1,j)
    if ((i-1>=0 and i-1<=maze.row and j>=0 and j<=maze.col)\
       and ((ways3[i][j]==2 and (ways3[i-1][j]==3 or ways3[i-1][j]==2))\
       or (ways3[i][j]==1 and (ways3[i-1][j]==3 or ways3[i-1][j]==2))\
           or (ways3[i][j]==3 and (ways3[i-1][j]==3 or ways3[i-1][j]==2)))):
               ways4[i][j]=0
               #print(i,j,'u')
               find_walls(i-1,j)
    if ((i>=0 and i<=maze.row and j>=0 and j+1<=maze.col)\
       and ((ways3[i][j]==1 and ways3[i][j+1]!=0)\
        or (ways3[i][j]==3 and ways3[i][j+1]!=0))):
               ways4[i][j]=0
               #print(i,j,'r')
               find_walls(i,j+1)
    if ((i>=0 and i<=maze.row and j-1>=0 and j-1<=maze.col)\
       and ((ways3[i][j]==1 and (ways3[i][j-1]==3 or ways3[i][j-1]==1))\
        or (ways3[i][j]==2 and (ways3[i][j-1]==1 or ways3[i][j-1]==3))\
            or (ways3[i][j]==3 and (ways3[i][j-1]==3 or ways3[i][j-1]==1)))):
               ways4[i][j]=0
               #print(i,j,'l')
               find_walls(i,j-1)
    if ((i>=0 and i-1<=maze.row and j>=0 and j+1<=maze.col)\
        and ((ways3[i][j]==1 and (ways3[i-1][j+1]==3 or ways3[i-1][j+1]==2))\
            or (ways3[i][j]==3 and (ways3[i-1][j+1]==3 or ways3[i-1][j+1]==2)))):
               ways4[i][j]=0
               #print(i,j,'ru')
               find_walls(i-1,j+1)
    if ((i>=0 and i+1<=maze.row and j>=0 and j-1<=maze.col)\
        and ((ways3[i][j]==2 and (ways3[i+1][j-1]==3 or ways3[i+1][j-1]==1))\
            or (ways3[i][j]==3 and (ways3[i+1][j-1]==3 or ways3[i+1][j-1]==1)))):
               ways4[i][j]=0
               #print(i,j,'ld')
               find_walls(i+1,j-1)        
wallsests()
#print(wallNum)
GateNum=len(maze.gates)
if isPrint:
    print('The maze has '+transNum(GateNum)+' gate'+getS(GateNum)+'.')
    print('The maze has '+transNum(wallNum)+' set'+getS(wallNum)+' of walls that are all connected.')
    print('The maze has '+transNum(inaccNum)+' inaccessible inner point'+getS(inaccNum)+'.')
    print('The maze has '+transNum(areaNum)+' accessible area'+getS(areaNum)+'.')
    print('The maze has '+transNum(culNum)+' set'+getS(culNum)+' of accessible cul-de-sacs that are all connected.')
    print('The maze has '+transNum(len(allroute))+' entry-exit path'+getS(len(allroute))+' with no intersection'+getS(len(allroute))+' not to cul-de-sacs.')
    #print(allroute)          
fileName=fileName.split('.')[0]+'.tex'
f=open(fileName,'w')
f.write('\\documentclass[10pt]{article}\n')
f.write('\\usepackage{tikz}\n')
f.write('\\usetikzlibrary{shapes.misc}\n')
f.write('\\usepackage[margin=0cm]{geometry}\n')
f.write('\\pagestyle{empty}\n')
f.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
f.write('\n')
f.write('\\begin{document}\n')
f.write('\n')
f.write('\\vspace*{\\fill}\n')
f.write('\\begin{center}\n')
f.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')
f.write('% Walls\n')
for i in range(row+1):
    start=False
    for j in range(col+1):
        if wall[i][j]==1 or wall[i][j]==3:
            if not start:
                f.write('    \\draw ('+str(j)+','+str(i)+')')
                start=True
        else:
            if start:
                f.write(' -- ('+str(j)+','+str(i)+');\n')
                start=False
for j in range(col+1):
    start=False
    for i in range(row+1):
        if wall[i][j]==2 or wall[i][j]==3:
            if not start:
                f.write('    \\draw ('+str(j)+','+str(i)+')')
                start=True
        else:
            if start:
                f.write(' -- ('+str(j)+','+str(i)+');\n')
                start=False

f.write('% Pillars\n')
for i in range(row+1):
    for j in range(col+1):
        if wall[i][j]==0:
            start=False
            if ((i>0 and (wall[i-1][j]==1 or wall[i-1][j]==0)) or i==0)\
            and ((j>0 and (wall[i][j-1]==2 or wall[i][j-1]==0)) or j==0):
                f.write('    \\fill[green] ('+str(j)+','+str(i)+')')
                f.write(' circle(0.2);\n')
f.write('% Inner points in accessible cul-de-sacs\n')
for i in range(row):
    for j in range(col):
        if marked[i][j]==-1:
            f.write('    \\node at ('+str(j+0.5)+','+str(i+0.5)+')')
            f.write(' {};\n')   
f.write('% Entry-exit paths without intersections\n')
for i in range(row):
    start=False
    for j in range(col):
        if marked[i][j]==5:
            if (maze4.maze[i][j].left==True and maze4.maze[i][j].right==True):                
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j-0.5)+','+str(i+0.5)+')')
                    start=True
            if (maze4.maze[i][j].left==False and maze4.maze[i][j].right==True):
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j+0.5)+','+str(i+0.5)+')')
                    start=True
            if (maze4.maze[i][j].left==True and maze4.maze[i][j].right==False):
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j-0.5)+','+str(i+0.5)+')')
                    start=True
                if start:
                    f.write(' -- ('+str(j+0.5)+','+str(i+0.5)+');\n')
                    start=False
        else:
            if start:
                f.write(' -- ('+str(j+0.5)+','+str(i+0.5)+');\n')
                start=False
        if j==col-1 and start:
            f.write(' -- ('+str(j+1.5)+','+str(i+0.5)+');\n')
for j in range(col):
    start=False
    for i in range(row):
        if marked[i][j]==5:
            if (maze4.maze[i][j].up==True and maze4.maze[i][j].down==True):                
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j+0.5)+','+str(i-0.5)+')')
                    start=True
            if (maze4.maze[i][j].up==False and maze4.maze[i][j].down==True):
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j+0.5)+','+str(i+0.5)+')')
                    start=True
            if (maze4.maze[i][j].up==True and maze4.maze[i][j].down==False):
                if not start:
                    f.write('    \\draw[dashed, yellow] ('+str(j+0.5)+','+str(i-0.5)+')')
                    start=True
                if start:
                    f.write(' -- ('+str(j+0.5)+','+str(i+0.5)+');\n')
                    start=False
        else:
            if start:
                f.write(' -- ('+str(j+0.5)+','+str(i+0.5)+');\n')
                start=False
        if i==row-1 and start:
            f.write(' -- ('+str(j+0.5)+','+str(i+1.5)+');\n')
f.write('\\end{tikzpicture}\n')
f.write('\\end{center}\n')
f.write('\\vspace*{\\fill}\n')
f.write('\n')
f.write('\\end{document}\n')



