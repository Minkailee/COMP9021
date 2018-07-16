import sys
order=['first','second','third']
string=[]
for i in range(len(order)):
    string.append(input('Please input the {} string:'.format(order[i])))
last=0
if len(string[1])>len(string[0]):
    last=1
if len(string[2])>len(string[1]):
    last=2
if last==0:
    first=1
    second=2
elif last==1:
    first=0
    second=2
else:
    first=0
    second=1
if (len(string[first])+len(string[second]))!=len(string[last]):
    print('Incorrect input!')
    sys.exit()
def sol(first,second,last):
    if not first and second==last:
        return True
    if not second and first==last:
        return True
    if not first or not second:
        return False
    if (first[0]==last[0]) and sol(first[1:],second,last[1:]):
        return True
    if (second[0]==last[0]) and sol(first,second[1:],last[1:]):
        return True
    return False
def tras(word):
    if word==0:
        return 'first'
    elif word==1:
        return 'second'
    else:
        return 'third'
if sol(string[first],string[second],string[last]):
    print('The {} string can be obtained by merging the other two'.format(tras(last)))
else:
    print('There is no sol')
