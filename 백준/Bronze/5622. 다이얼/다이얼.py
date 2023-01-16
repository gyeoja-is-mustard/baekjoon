a = input()
table = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','22233344455566677778889999')
b = a.translate(table)
result = 0
for i in range(len(b)):
    result += int(b[i])
print(result+len(b))