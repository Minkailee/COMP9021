def odd(n):
    if n%2==0:
        return False
    else:
        return True
for i in range(100,989):
    if odd(i) or odd(i//10) or (not odd(i//100)):
        continue
    else:
        for j in range(20,89):
            if odd(j) or odd(j//10):
                continue
            else:
                result1=i*(j%10)
                if result1<1000 or result1>9999:
                    continue
                if odd(result1) or odd(result1//10) or (not odd(result1//100)) or odd(result1//1000):
                    continue
                else:
                    result2=i*(j//10)
                    if result2<100 or result2>999:
                        continue
                    if odd(result2) or (not odd(result2//10)) or odd(result2//100):
                        continue
                    else:
                        result3=i*j
                        if result3<1000 or result3>9999:
                            continue
                        if odd(result3) or odd(result3//10) or (not odd(result3//100)) or (not odd(result3//1000)):
                            continue
                        else:
                            print(' {}'.format(i))
                            print('x {}'.format(j))
                            print(' ---')
                            print(result1)
                            print(result2)
                            print('----')
                            print(result3)
                        
