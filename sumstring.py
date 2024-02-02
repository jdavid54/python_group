def sum(s):
	result=0
	for i in s:
		result+=int(i)
	return result
	
def sum2(s):
		return sum(list(s))
		
print(sum2(input()))