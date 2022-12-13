def pr(n, i):
	if (n < 2):
		return 'No'
	elif (n == 2):
		return 'Yes'
	elif (n % i == 0):
		return 'No'
	elif (i < n / 2): 
		return pr(n, i + 1)
	else:
		return 'Yes'
		
n=int(input('Введите число: '))
i=2			
print(pr(n, i))
