a=[]
with open('Kozyreva_E.S._Um-222_vvod.txt','r') as f1:
	for line in f1.readlines():
		b=line.replace('\n','').split()
		for i in range(len(b)):
			b[i]=int(b[i])
		a.append(b)
	print(a)
	print('Матрица: ')
	 		
for i in range(len(a)):
	for j in range(len(a[i])):
		print(a[i][j], end=' ')
	print()			

with open('Kozyreva_E.S._Um-222_vivod.txt','w') as f2:
	for i in range(len(a)):
		max=a[i][j]
		for j in range(len(a)):
			if max<a[i][j]:
				max=a[i][j]
		print('Наибольший в',i+1, 'строке:', max)		
		f2.write('Наибольший в '+str(i+1)+ ' строке:'+str(max)+'\n')			
	print()
	f2.write('\n')
	for i in range(len(a)):
		min=a[j][i]
		for j in range(len(a)):
			if min>a[j][i]:
				min=a[j][i]
		print('Наименьший в',i+1, 'столбце:', min)
		f2.write('Наименьший в '+str(i+1)+ ' столбце:'+str(min)+'\n')
	print()
	
