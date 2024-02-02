n =0.5684756847
#n=0.7878
#n = 0.333
#n=0.1234512345

for k in range(1,10):
	value = n*10**k
	z= round(value-int(value),k)
	rep = z*10**k
	#print(value,z,rep)
	#print(value,int(value),z,rep)
	
	if int(value) == rep:break

def reduc(n,p):
	for i in range(2,p):
		
		if n%i==0 and p%i==0:
			n//=i
			p//=i
		if n==1:break
	#print(i,n,p)
	return n,p

#print(reduc(15,75))

num=int(value)
denom=10**k-1

num,denom=reduc(num,denom)
print(n,'=',num,'/',denom)	