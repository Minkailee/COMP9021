import sys
import re
ID=input('Which data file do you want to use?')
try:
    file=open(ID)
    Lall=[]
    for line in file:
        line=re.split(r"['R()\n']",line)
        l=line[2].split(',')
        #print(l)
        Leach=[int(l[0]),int(l[1])]
        Lall.append(Leach)
    #print(Lall)
    file.close()
    if Leach==[] or Lall==[]:
        raise ValueError
except ValueError:
    print('Incorrect input, exiting!')
    sys.exit()
except IOError:
    print('Incorrect input, exiting!')
    sys.exit()

route={}
Lstart=[]
Lend=[]
for x in Lall:
    Lstart.append(x[0])
    if x[0] in route:
        route[x[0]].append(x[1])
    else:
        route[x[0]]=[x[1]]
Lstart=set(Lstart)
for x in Lall:
    if x[1] not in Lstart:
        Lend.append(x[1])
Lend=set(Lend)
#print(route)
#print(Lstart)
#print(Lend)


def find_all_paths(route, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in route:
        return []
    paths = []
    for node in route[start]:
        if node not in path:
            newpaths = find_all_paths(route, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
nonredundant=[]
for i in Lstart:
    for j in Lend:
            start=i
            end=j
            paths=find_all_paths(route, start, end, path=[])
            #print(paths)
            if not paths==[]:
                longest=1
                for item in paths:
                    if int(len(item))>longest:
                        longest=int(len(item))
                        best=item
                for k in range(int(len(best)-1)):
                    step=[best[k],best[k+1]]
                    if step not in nonredundant:
                        nonredundant.append(step)
print('The nonredundant facts are:')
for item in Lall:
    if item in nonredundant:
        step1=(int(item[0]),int(item[1]))
        print('R({},{})'.format(step1[0],step1[1]))
