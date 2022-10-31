"""Дана целочисленная квадратная матрица. Найти в каждой строке 
наибольший элемент и в каждом столбце наименьший. Вывести на 
экран"""
from random import*
n=4
a=[]
for i in range (n):
	b=[]
	for j in range (n):
		b.append(randint(0,20))
	a.append(b)
for i in range(n):
	for j in range(n):
		print(a[i][j], end=' ')
	print()			

for i in range(n):
	max=a[i][j]
	for j in range(n):
		if max<a[i][j]:
			max=a[i][j]
	print('Наибольший в',i+1, 'строке:', max)	
print()	

"""for i in range(n):
	for j in range(n):
		print(a[j][i], end=' ')
	print()	"""

for i in range(n):
	min=a[j][i]
	for j in range(n):
		if min>a[j][i]:
		   min=a[j][i]
	print('Наименьший в',i+1, 'столбце:', min)


