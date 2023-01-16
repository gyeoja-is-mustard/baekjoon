N = int(input())
n = 0
if N % 5 == 0: 
    print(N//5)
else:
    while N % 5 != 0 and N>=0: 
        N -= 3
        n += 1
    if N < 0:
        print(-1)
    else:
        print(n+N//5)