'''

'''
from numpy import sqrt

max = 1000000
odds=[]
primes = []
ops=0
tries = []
debug = False

def dummy(*args, **kargs): pass

if not debug: 
    #don't print
    xprint = dummy
else:
    #please print for debug
    xprint = print

print(f"Searching primes under {max}")
last_n = 2
pairs = []

for n in range(3,max,2):   #candidates = all odds from 3 to max
    if n%10==5:continue
    prime = True    
    count = 0
    for k in primes:  # division by all known primes
        if k>sqrt(n):break
        ops+=1
        count += 1
        xprint(primes,sqrt(n),k>sqrt(n))
        xprint(n,k,n%k==0,end="")
        if (n%k) == 0:
            prime = False
            xprint()
            xprint(n," is not prime!")           
            xprint()
            break  # next n if n is not prime 
        else:
            xprint()
    
    # after divisions with all primes or if n not prime   
    if prime:
        xprint(n," is prime !")
        if n not in primes:
            primes.append(n)
        xprint()
        if last_n+2==n:
            pairs.append((last_n, n))            
        last_n = n
    tries.append(count)
    
    
primes = [2] + primes               
#xprint(odds)
print(primes)
print(ops)
xprint(pairs)
xprint(len(primes),len(tries))

import numpy as np
flat=list(set(np.array(pairs).flatten()))
flat.sort()
#print(flat)

import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(tries)
ax1.set_title("Tries")
ax2.scatter(flat,flat,marker=".",s=2)
ax2.set_title("Pairs")
fig.tight_layout()
plt.show()

def save_primes():
    #save once
    import pickle
    with open('1Mprimes.pkl', 'wb') as f:
        pickle.dump(primes, f)

def load_primes():
    #save once
    import pickle
    with open('1Mprimes.pkl', 'rb') as f:
        pickle.load(primes, f)