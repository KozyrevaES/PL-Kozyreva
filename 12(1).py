def pr(n):
    for i in range(2, n):
        if n%i==0:
            return 'No'
        else:
           return 'Yes'
    
n=int(input('Введите число: '))
print(pr(n))
