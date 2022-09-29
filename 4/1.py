a = int(input('Введите целое число a='))
b = int(input('Введите целое число(a<=b) b='))
if a<=b:
	for i in range(a, b+1):
		print(i,end = ";")
else:
	print('Ошибка(a>=b)')		
