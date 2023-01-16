A, B, C = map(int, input().split())
if B < C:
    N = int(A/(C-B))+1
else:
    N = -1
print(N)
