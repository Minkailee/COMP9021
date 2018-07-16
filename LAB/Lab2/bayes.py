from random import choice
while True:
    try:
        times = int(input('Enter the number of times a randomly chosen die will be cast:'))
        if times <= 0:
            raise ValueError
        break
    except ValueError:
            print('Your input is incorrect, try again.')
#a1--a5为骰子
a1=range(1,5)#4面
a2=range(1,7)#6面
a3=range(1,9)#8面
a4=range(1,13)#12面
a5=range(1,21)#20面
a=[a1,a2,a3,a4,a5]
step1=choice(a)#选骰子
print('This is a secret, but the chosen die is the one with',step1[-1],'faces.\n')
#以下列表第一项对应1-4，第二项对应5-6，第三项对应7-8，第四项对应9-12，第五项对应13-20：
La=[1/5*(1/4+1/6+1/8+1/12+1/20),1/5*(1/6+1/8+1/12+1/20),1/5*(1/8+1/12+1/20),1/5*(1/12+1/20),1/5*1/20]
#P(A)投出面为*的概率
Lb=[1/5]*5
#P(B)选择*骰子的概率
Lc=[1/4,1/6,1/8,1/12,1/20]
#P（A|B）
for i in range(times):
    upface=choice(step1)#扔骰子
    #分类讨论：
    if upface>=1 and upface<=4:
        p4=Lb[0]/4/La[0]
        p6=Lb[1]/6/La[0]
        p8=Lb[2]/8/La[0]
        p12=Lb[3]/12/La[0]
        p20=Lb[4]/20/La[0]
    if upface==5 or upface==6:
        p4=0.0
        p6=Lb[1]/6/La[1]
        p8=Lb[2]/8/La[1]
        p12=Lb[3]/12/La[1]
        p20=Lb[4]/20/La[1]
    if upface==7 or upface==8:
        p4=0.0
        p6=0.0
        p8=Lb[2]/8/La[2]
        p12=Lb[3]/12/La[2]
        p20=Lb[4]/20/La[2]
    if upface>=9 and upface<=12:
        p4=0.0
        p6=0.0
        p8=0.0
        p12=Lb[3]/12/La[3]
        p20=Lb[4]/20/La[3]
    if upface>=13 and upface<=20:
        p4=0.0
        p6=0.0
        p8=0.0
        p12=0.0
        p20=Lb[4]/20/La[4]
    #更新P（B）：
    Lb=[p4,p6,p8,p12,p20]
    j=0
    #更新P（A）：
    while True:
        sum=0
        for k in range(j,5):
            sum=sum+(Lb[k]*Lc[k])
        La[j]=sum
        j=j+1
        if j==5:
            break
    print('Casting the chosen die... Outcome:',upface)
    print('The updated dice probabilities are:\n\n')
    print(' 4:{:4.2f}'.format(p4*100)+'%')
    print(' 6:{:4.2f}'.format(p6*100)+'%')
    print(' 8:{:4.2f}'.format(p8*100)+'%')
    print('12:{:4.2f}'.format(p12*100)+'%')
    print('20:{:4.2f}'.format(p20*100)+'%')
