a=[]
with open('Kozyreva_E.S._Um-222_vvod(2).txt','r') as f1:
	for line in f1.readlines():
		b=line.replace('\n','').split()
		for i in range(len(b)):
			b[i]=float(b[i])
		a.append(b)
	print(a)
	print('Исходная матрица: ')
	 		
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j], end=' ')
	print()			

b = sum(a, [])
max1 = max(b[::len(a)+1])
max2 = max(b[len(a)-1::len(a)-1][:len(a)])
if max1 > max2:
    i1 = j1 = b[::len(a)+1].index(max1)
else:
    i1 = b[len(a)-1::len(a)-1][:len(a)].index(max2)
    j1 = len(a) - 1 - i1
a[len(a)//2][len(a)//2], a[i1][j1] = a[i1][j1], a[len(a)//2][len(a)//2]
 
with open('Kozyreva_E.S._Um-222_vivod(2).txt','w') as f2:
	f2.write('Результат: \n')
	for i in a:
		print(i)
		f2.write(str(i)+'\n')
