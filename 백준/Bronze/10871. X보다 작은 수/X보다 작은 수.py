N, X = map(int,input().split())
A = list(map(int, input().split()))
result = []
for i in A:
    if i < X:
        i = str(i)
        result.append(i)
answer = " ".join(result)
print(answer)