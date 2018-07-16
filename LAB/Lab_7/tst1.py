import sys
banknotes=[1,2,5,10,20,50,100]
try:
    desired=int(input('Input the desired amount:'))
    if desired<0:
        raise ValueError
except ValueError:
    print('Incorrect input!')
    sys.exit()
usage=[]
count=0
while desired>0:
    value=banknotes.pop()
    if desired>value:
        usage.append((value,desired//value))
        count+=desired//value
        desired=desired-value*(desired//value)
    if banknotes==[]:
        break
if desired==0:
    print('{} banknotes are needed'.format(count))
    print('The detail is:')
    for value in usage:
        print('{:>4}:{}'.format('$'+str(value[0]),value[1]))
