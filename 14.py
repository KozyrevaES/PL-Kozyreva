f = open('StudentsPerformance 14.csv')

k = 0
for line in f:
    info = line.split(',')
    if info[0] == '"female"':
        if info[2] == '"some college"':
            k+=1
print('у ',k,' девочек')
f.close()
