M = int(input())
N = int(input())
prime = []
for i in range(M, N+1):
    criteria = 0
    if i != 1:
        for j in range (2, i):
            if i%j == 0:
                criteria = 1
        if criteria == 0:
            prime.append(i)
if prime == []:
    print(-1)
else:
    print(sum(prime))
    print(min(prime))