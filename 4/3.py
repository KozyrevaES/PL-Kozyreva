a = int(input('Введите целое число a='))
b = int(input('Введите целое число(a>b) b='))
if a>b:
	for i in range(a - (a + 1) % 2, b - b % 2, -2):
		print(i,end = ";")
else:
	print('Ошибка(a>=b)')		
