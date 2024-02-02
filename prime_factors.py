def prime_factor(n):
    factors = []
    count = 0
    for i in range(2,int(n**.5)):
        if n%i == 0:
            factor = True
            #print(i,i//2 + 1, end='-')
            for j in range(2, (i//2 + 1)):
                #print(j,end=' ')
                if (i%j == 0):
                    factor = False
                    break
            if factor:
                #print('=',i)
                factors.append(i)
    return factors

n = '2**3 * 7**5 * 11**3 * 13 * 17'

factors = prime_factor(eval(n))
print(n,'\nfactors:',factors)

def factorize(n):
    factors = []
    powers = {}
    for i in range(2,int(n**.5)):        
        # find the factor
        if n%i == 0:
            factor = True
            #print(i,int(i**.5), end='-j=')
            # test if i is prime
            for j in range(2, int(i**.5)):
                #print(j,end=',')
                if i%j == 0:
                    factor = False                   
                    break
            #print()
            if factor:
                # find the powers
                while n%i==0 and n>1:
                    #print('=',n,i)
                    if str(i) in powers.keys():
                        powers[str(i)] += 1
                    else:
                        powers[str(i)] = 1
                    n=n//i
                factors.append(i)
    return factors, powers

factors,powers = factorize(eval(n))
print('\nfactors:',factors,'\npowers:',powers)