print("Input pairs of the form 'value : number' to indicate that you have\n"
      "'number' many banknotes of face value 'value'.")
print('Input these pairs one per line, with a blank line '
      'to indicate end of input.\n')
def print_solution(solution):
    length=max(len(str(value)) for value in solution)
    for value in sorted(solution.keys()):
        print('{:>{:}}: {:}'.format('$'+str(value),length,solution[value]))
note_value=[]
while True:
    line=input()
    if ':' not in line:
        break
    value,amount=line.split(':')
    note_value.append((int(value),int(amount)))
note_value=sorted(note_value,key=lambda t:t[0])
note_value.reverse()
desired = int(input('Input the desired amount: '))
minimal_comb=[[0,[]]]+[[float('inf'),[]] for i in range(desired)]
#print(len(minimal_comb))
for sub_amount in range(1,desired+1):
    for i in range(len(note_value)):
        value=note_value[i][0]
        if sub_amount<value:
            continue
        if sub_amount==value:
            minimal_comb[sub_amount]=[1,[{value:1}]]
            break
        print(sub_amount,value)
        if minimal_comb[sub_amount-value][0]>=minimal_comb[sub_amount][0]:
            continue
        #print(minimal_comb)
        for option in minimal_comb[sub_amount-value][1]:
            if value not in option or option[value]<note_value[i][1]:
                if minimal_comb[sub_amount-value][0]+1<minimal_comb[sub_amount][0]:
                    minimal_comb[sub_amount][0]=minimal_comb[sub_amount-value][0]+1
                    minimal_comb[sub_amount][1].clear()
                extened_option=dict(option)
                if value not in option:
                    extened_option[value]=1
                else:
                    extened_option[value]+=1
                if extened_option not in minimal_comb[sub_amount][1]:
                    minimal_comb[sub_amount][1].append(extened_option)
minimal_nb_of_banknotes = minimal_comb[desired][0]
print(minimal_comb)
if minimal_nb_of_banknotes==float('inf'):
    print('There is no solution.')
else:
    solutions=minimal_comb[desired][1]
    solutionsnb=len(solutions)
    if solutionsnb==1:
        print('\nThere is a unique solution:')
        print_solution(solutions[0])
    else:
        print('\nThere are {} solutions:'.format(solutionsnb))
        for i in range(solutionsnb - 1):
            print_solution(solutions[i])
            print()
        print_solution(solutions[solutionsnb - 1])

