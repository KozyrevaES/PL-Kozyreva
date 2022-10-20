def evkl(a,b):
	while a!=0 and b!=0:
		if a>=b:
			a%=b
		else:
			b%=a
	return a or b
def nok(a,b):
	return (a*b)/evkl(a,b)
a=int(input('a='))
b=int(input('b='))
l=nok(a,b)
k=evkl(a,b)
print('НОД',k)
print('НОК',int(l))					
