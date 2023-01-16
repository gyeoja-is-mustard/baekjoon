N = int(input())
for i in range(N):
    a, b = input().split()
    c =''    
    for j in range(len(b)):
        c += b[j]*int(a)
    print(c)