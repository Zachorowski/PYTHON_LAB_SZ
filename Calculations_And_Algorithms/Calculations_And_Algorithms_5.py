from random import randint

temp = []
row = []
A = []
B = []
C = []

for i in range(8):
    for j in range(8):
        row.append(randint(0,10))
    A.append(row)
    row = []

for i in range(8):
    for j in range(8):
        row.append(randint(0,10))
    B.append(row)
    row = []

for i in range(8):
    for j in range(8):
        for k in range(8):
            temp.append(A[i][j]+B[k][j])
        row.append(sum(temp))
        temp = []
    C.append(row)
    row = []


print(A)
print(B)
print(C)