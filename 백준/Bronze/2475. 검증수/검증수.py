a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    b.append(a[i]**2)
print(sum(b)%10)