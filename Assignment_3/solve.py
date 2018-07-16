import sys, os, copy, re

def mainfunc():
    global name_map_global
    puzzle = ""
    puzzle_list = []
    text = input("Which text file do you want to use for the puzzle? ")
    with open(text, "r") as f:
        for line in f:
            # print(line)
            puzzle = puzzle.strip("\n") + str(line).strip("\n") + " "
    f.close()
    names=findname(puzzle)
    if names==[]:
        print('Incorrect input!')
        sys.exit
    claims=findclaim(puzzle,names)
    if claims=={}:
        print('Incorrect input!')
        sys.exit
    finallsol=solve(claims,names)
    printresults(names,finallsol)
    
def findname(puz):
    puz=re.split(' |,',puz)
    puz1=[]
    for words in puz:
        word=''
        for letter in words:
            if letter.isalpha():
              word=word+letter
        if word!='':
            puz1.append(word)
    #-----------devide text into words and get rid of punctuations
    #print(puz1)
    names=[]
    for i in range(len(puz1)-1):
        if puz1[i]=='Sir' and (puz1[i+1] not in names) and puz1[i+1][0].isupper():
            names.append(puz1[i+1])
        if puz1[i]=='Sirs':
            j=i+1
            while puz1[j]!='and' and (puz1[j] not in names)and puz1[j][0].isupper():
                names.append(puz1[j])
                j+=1
            if puz1[j+1] not in names and puz1[j+1][0].isupper():
               names.append(puz1[j+1]) 
    names=sorted(names)
    #------------using 'Sir' and 'Sirs' to locate each name
    #print(names)
    return names

def findclaim(puz,names):
    claims={}
    stences=[]
    start=0
    end=0
    while end < len(puz)-1:
        if (puz[end] == '.' or puz[end] == '!'or puz[end]=='?') and puz[end+1] == '"':
            stences.append(puz[start:end+2])
            start = end + 2
        elif puz[end] == '.' or puz[end] == '!' or puz[end]=='?':
            stences.append(puz[start:end+1])
            start = end + 1
        end += 1
    #-----------------divide text into stences
    #print(stences)
    for stence in stences:
        if '"'in stence:
            index1=stence.find('"')
            front=stence[:index1]
            leftstence=stence[index1+1:]
            index2=leftstence.find('"')
            claim=leftstence[:index2]
            #print(claim)
            while not claim[-1].isalpha():
                claim=claim[:-1]
            #print(claim)
            after=leftstence[index2:]
            rest=(front+after).split()
            #print(rest)
            rest1=[]
            for words in rest:
                word=''
                for letter in words:
                    if letter.isalpha():
                      word=word+letter
                if word!='':
                    rest1.append(word)
            for word in rest1:
                if word in names:
                    name=word
            claim1=[]
            for words in claim.split():
                word=''
                for letter in words:
                    if letter.isalpha():
                      word=word+letter
                if word!='':
                    claim1.append(word)
            #print(claim1)
            for i in range(len(claim1)):
                if claim1[i]=='I':
                    claim1[i]='Sir '+name
                    #print(claim[i])
                claim=''
                for words in claim1[:-1]:
                    claim+=words+' '
                claim+=claim1[-1]
            if name in claims:
                claims[name].append(claim)
            else:
                claims[name]=[claim]
            #print(name+': ',claim)
    #----------------seach the claim in each stence
    #print(claims)
    return claims

def solve(claims,names):
    numb=2**(len(names))
    allcase=[]
    for i in range(numb):
        case=[]
        comb=bin(i)[2:]
        for x in comb:
            case.append(int(x))
        while len(case)<len(bin(numb-1)[2:]):
            case.insert(0,0)
        allcase.append(tuple(case))
    #print(allcase,len(allcase))
    #---------------------------------------get all the combinations.
    solution={}
    speakernames=[]
    for name in claims:
        #print(name+': ',claims[name])
        index=names.index(name)+1
        #print(name,index)
        solution[index]=[]
        solution[-index]=[]
        for claim in claims[name]:
            claim=claim.replace(',',' ')
            #print(claim)
            mentioned=[]
            divided=claim.split()
            for i in range(len(divided)-1):
                if divided[i]=='Sir':
                    mentioned.append(names.index(divided[i+1]))
                if divided[i]=='us':
                    for k in range(len(names)):
                        mentioned.append(k)
                    break
            #print(mentioned)
            useless=[]
            if mentioned==[]:
                useless.append(name)
                continue
            #-------------------------------find the names mentioned in the claim
            if claim.startswith('at least') or claim.startswith('At least') or 'or' in claim:
                #-----At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
                #-----& Disjunction_of_Sirs is a Knight/Knave
                if claim.endswith('Knight'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum>0 and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum==0 and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if claim.endswith('Knave'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum<len(mentioned) and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    if index-1 not in mentioned:#-----Knive can't say self is a Knive 
                        for x in allcase:
                            sum=0
                            for i in mentioned:
                                sum+=x[i]
                            if sum==len(mentioned) and x[index-1]==0:
                                temp.append(x)
                    solution[-index].append(temp)
                if index not in speakernames:
                    speakernames.append(index)
            elif claim.startswith('at most') or claim.startswith('At most'):
                #-----At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
                if claim.endswith('Knight'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum<=1 and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum>1 and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if claim.endswith('Knave'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum>=(len(mentioned)-1) and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum<(len(mentioned)-1) and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if index not in speakernames:
                    speakernames.append(index)
            elif claim.startswith('Exactly') or claim.startswith('exactly'):
                #------Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
                if claim.endswith('Knight'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum==1 and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum!=1 and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if claim.endswith('Knave'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum==(len(mentioned)-1) and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum!=(len(mentioned)-1) and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if index not in speakernames:
                    speakernames.append(index)
            elif claim.endswith('Knights') or claim.endswith('Knaves'):
                #------All/all of us are Knights/Knaves & Conjunction_of_Sirs are Knights/Knaves
                if claim.endswith('Knights'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum==len(mentioned) and x[index-1]==1:
                            temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum!=len(mentioned) and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if claim.endswith('Knaves'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    if index-1 not in mentioned:#---Knight can't say self Knave
                        for x in allcase:
                            sum=0
                            for i in mentioned:
                                sum+=x[i]
                            if sum==0 and x[index-1]==1:
                                temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        sum=0
                        for i in mentioned:
                            sum+=x[i]
                        if sum>0 and x[index-1]==0:
                            temp.append(x)
                    solution[-index].append(temp)
                if index not in speakernames:
                    speakernames.append(index)
            elif claim.startswith('Sir') and (claim.endswith('Knight') or claim.endswith('Knave')):
                #------I am a Knight/Knave & Sir Sir_Name is a Knight/Knave
                if claim.endswith('Knight'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    for x in allcase:
                        for i in mentioned:
                            if x[i]==1 and x[index-1]==1:
                                temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    for x in allcase:
                        for i in mentioned:
                            if x[i]==0 and x[index-1]==0:
                                temp.append(x)
                    solution[-index].append(temp)
                if claim.endswith('Knave'):
                    #solution[index]=[]#-----speaker is a Knight
                    temp=[]
                    if index-1 not in mentioned:#---Knight can't say self Knave
                        for x in allcase:
                            for i in mentioned:
                                if x[i]==0 and x[index-1]==1:
                                    temp.append(x)
                    solution[index].append(temp)
                    #solution[-index]=[]#-----speaker is a Knive
                    temp=[]
                    if index-1 not in mentioned:#---Knave can't say self Knave
                        for x in allcase:
                            for i in mentioned:
                                if x[i]==1 and x[index-1]==0:
                                    temp.append(x)
                    solution[-index].append(temp)
                if index not in speakernames:
                    speakernames.append(index)
            else:
                 useless.append(name)
                 continue
        temp1=[]
        count=0
        for temp in solution[index]:
            temp2=[]
            if len(temp)==0:
                temp1=[]
                break
            count+=1
            temp1+=temp
            if count>1:
                for x in temp1:
                    if temp1.count(x)==2 and x not in temp2:
                        temp2.append(x)
                temp1=temp2
        solution[index]=temp1
        temp1=[]
        count=0
        
        for temp in solution[-index]:
            temp2=[]
            if len(temp)==0:
                temp1=[]
                break
            count+=1
            temp1+=temp
            if count>1:
                for x in temp1:
                    if temp1.count(x)==2 and x not in temp2:
                        temp2.append(x)
                temp1=temp2
        solution[-index]=temp1 
    #--------------------------------find out solution matching each person's all claims                       
    #print(solution)
    #print(speakernames)
    #print(useless)
    for x in useless:
        if useless.count(x)==len(claims[x]):
            del claims[x]
    #for name in claims:
        #for claim in claims[name]:
            #print(name+': ',claim)
    finallsol=[]
    numb=len(speakernames)
    if numb==1:
        for key in solution:
            for item in solution[key]:
                finallsol.append(item)
    else:
        all_claimcob=[]
        for i in range(2**numb):
            cob=[]
            claimcob=[]
            case=bin(i)[2:]
            for x in case:
                cob.append(int(x))
            while len(cob)<len(bin(2**numb-1)[2:]):
                cob.insert(0,0)
            for i in range(len(cob)):
                if cob[i]==0:
                    claimcob.append(-speakernames[i])
                else:
                    claimcob.append(speakernames[i])
            all_claimcob.append(tuple(claimcob))
        #print(all_claimcob)
        for claimcob in all_claimcob:
            #print(claimcob)
            sol=[]
            #sol1=[]
            count=0
            for claim in claimcob:
                count+=1
                temp=[]
                if len(solution[claim])==0:
                    sol=[]
                    break
                sol+=solution[claim]
                #print(sol,claim)
                if count>1:
                    for x in sol:
                        if sol.count(x)==2 and x not in temp:
                            temp.append(x)
                    sol=temp
                    #print(sol)
            #print(sol)
            finallsol+=sol
        finallsol=set(finallsol)
    finall=[]
    for x in finallsol:
        finall.append(x)
        #--------------------------------find out solution matching all persons' claims
    #print(finall)
    return finall          

def printresults(names,finallsol):
    def transform(b):
        if b==0:
            return 'Knave'
        else:
            return 'Knight'
    print('The Sirs are: ',end='')
    for name in names[:-1]:
        print(name,end=' ')
    print(names[-1])
    numb=len(finallsol)
    if numb==0:
        print('There is no solution.')
    elif numb==1:
        print('There is a unique solution:')
        for i in range(len(names)):
            print('Sir {} is a {}.'.format(names[i],transform(finallsol[0][i])))
    else:
        print('There are {} solutions.'.format(numb))
mainfunc()

            
    
