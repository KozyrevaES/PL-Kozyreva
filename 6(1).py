print('Ввод элементов списка:')
x=[]
min=0
max=0
x=[int(input())for i in range(10)]
print(x)
k=x[9]
print('max=',k)
for i in range(10):
	if x[i]<k:
		min=min+1
for i in range(10):
	if x[i]>k:
		max=max+1
print('Количество элементов меньших max=', min)
print('Количество элементов больших max=', max)		
