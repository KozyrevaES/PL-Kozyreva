print('Ввод элементов массива:')
x=[]
sum=0
for i in range(10):
	print('Введите',i,'элемент:')
	x.append(int(input()))
print(x)
for i in range(10):
	if x[i]>5:
		sum=sum+x[i]
print('Сумма чисел больших 5=',sum)	
