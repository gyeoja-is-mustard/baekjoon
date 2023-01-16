N = int(input())
num = list(map(int,input().split()))
prime = 0
if 1 in num:
    num.remove(1)
    N -= 1
for i in range(N):
    a = 0
    for j in range(2,num[i]):
        if num[i]%j == 0:
            a = 1
    if a == 0:
        prime += 1
print(prime)