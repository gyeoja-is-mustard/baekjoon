N = int(input())
A = N
cycle = 0
while True:
    N = 10*(N%10)+(N//10+N%10)%10
    cycle += 1
    if A == N:
        print(cycle)
        break