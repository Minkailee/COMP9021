import math
N=100000
N_index = (N - 1) // 2
primes_sieve = [True] * (N_index + 1)
for n in range(1, (round(math.sqrt(N)) + 1) // 2):
    if primes_sieve[n]:
        for i in range(2 * n * (n + 1), N_index + 1, 2 * n + 1):
            primes_sieve[i] = False
list_of_primes = [2]
for n in range(1, N_index + 1):
    if primes_sieve[n] and 2 * n + 1>=10000:
        list_of_primes.append(2 * n + 1)
L=list_of_primes        
for k in range(len(L)-5):
    if L[k+1]==L[k]+2 and L[k+2]==L[k+1]+4 and L[k+3]==L[k+2]+6 and L[k+4]==L[k+3]+8 and L[k+5]==L[k+4]+10:
        print(L[k],L[k+1],L[k+2],L[k+3],L[k+4],L[k+5])
