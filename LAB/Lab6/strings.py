def merg(str1,str2,str3):
    if not str1 and str2==str3:
        return True
    elif not str2 and str1==str3:
        return True
    elif not str1 or not str2:
        return False
    elif str1[0]==str3[0] and merg(str1[1:],str2,str3[1:]):
        return True
    elif str2[0]==str3[0] and merg(str1,str2[1:],str3[1:]):
        return True
    return False
strings=[]
ordinals = 'first', 'second', 'third'
for i in ordinals:
    strings.append(input('Please input the {} string: '.format(i)))
last=0
if len(strings[1])>len(strings[0]):
    last=1
elif len(strings[2])>len(strings[1]):
    last=2
if last==0:
    first,second=1,2
elif last==1:
    first,second=0,2
else:
    first,second=0,1
if len(strings[last])!=len(strings[first])+len(strings[second])\
   or not merg(strings[first],strings[second],strings[last]):
    print('No solution')
else:
    print('The {} string can be obtained by merging the other two.'.format(ordinals[last]))
