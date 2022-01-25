a = [1,2,12,4]
b = [2,4,2,8]
c = []

for i in range(len(a)):
    c.append(a[i]*b[i])

result = sum(c)
print(result)