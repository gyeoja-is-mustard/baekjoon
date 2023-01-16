N = int(input())
ans = 0
for i in range(max(0,N-len(str(N))*9), N):
    if i + sum(map(int, str(i))) == N:
        ans = i
        break
print(ans)