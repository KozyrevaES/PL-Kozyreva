import math
def s(a,b,c,d):
	p=(a+b+c+d)/2
	k=math.sqrt((p-a)*(p-b)*(p-c)*(p-d))
	return k
a=int(input('AB='))
b=int(input('BC='))	
c=int(input('CD='))
d=int(input('AD='))
k=s(a,b,c,d)
print('S=',k)
