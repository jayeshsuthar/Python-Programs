x = [[6,3,7],
    [2,4,1],
    [8,4,3]]

y = [[2,1,6],
    [5,3,7],
    [2,9,7]]

result = [[],[],[]]

for i in range(len(x)):

    for j in range(len(y[0])):

        for k in range(len(y)):
            result += x[i][j] * y[k][j]

for i in result:
    print(r)
