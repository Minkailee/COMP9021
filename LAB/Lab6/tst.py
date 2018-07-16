import sys
try:
    available=int(input('Input a number that we will use as available digits:'))
    desirednum=int(input('Input a number that represents the desired sum:'))
    if available<0 or desirednum<0:
        raise ValueError
except ValueError:
    print('Incorrect input!')
    sys.exit()

def sol(available,desirednum):
    if available==0:
        if desirednum==0:
            return 1
        return 0
    if desirednum<0:
        return 0
    return (sol(available//10,desirednum)+sol(available//10,desirednum-available%10))
sol_num=sol(available, desirednum)
if sol_num==0:
    print('There is no sol')
elif sol_num==1:
    print('There is a unique sol')
else:
    print('There are {} sols'.format(sol_num))
