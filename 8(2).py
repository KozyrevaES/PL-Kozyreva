"""Дана действительная квадратная матрица порядка N (N — нечетное), 
все элементы которой различны. Найти наибольший элемент среди 
стоящих на главной и побочной диагоналях и поменять его местами с 
элементом, стоящим на пересечении этих диагоналей."""
n=3
a=[]
for i in range (n):
	b=[]
	for j in range (n):
		print('Введите [',i,',',j,'] элемент')
		b.append(float(input()))
	a.append(b)
for i in range(n):
	for j in range(n):
		print(a[i][j], end=' ')
	print()

b = sum(a, [])
max1 = max(b[::n+1])
max2 = max(b[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = b[::n+1].index(max1)
else:
    i1 = b[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
a[n//2][n//2], a[i1][j1] = a[i1][j1], a[n//2][n//2]
 
for i in a:
	print(i)
