N = int(input())
result = 0
if N >= 100:
    for i in range(100, N+1):
        if i//100 + i%10 == 2*((i%100)//10):
            result += 1
    print(result+99)
else:
    print(N)