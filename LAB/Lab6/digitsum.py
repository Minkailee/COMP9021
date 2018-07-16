import sys
def solve(available_digit, desired_sum):
    if desired_sum<0:
        return 0
    if available_digit==0:
        if desired_sum==0:
            return 1
        else:
            return 0
    return(solve(available_digit//10,desired_sum)+solve(available_digit//10,desired_sum-available_digit%10))
try:
    available_digit=int(input('input the available digit: '))
    desired_sum=int(input('input the desired sum:'))
    if available_digit<0 or desired_sum<0:
        raise ValueError
except ValueError:
    print('Incorrect input')
    sys.exit()
nub=solve(available_digit, desired_sum)
if nub==0:
    print('there is no solution.')
elif nub==1:
    print('there is an unique solution.')
else:
    print('there are {} solutions.'.format(nub))
