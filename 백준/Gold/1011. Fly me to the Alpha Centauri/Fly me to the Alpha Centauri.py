T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    l = B-A
    for j in range(l):
        if j**2 < l <= (j+1)**2:
            p = j
            break
    if p**2 < l <= p**2+p:
        print(2*p)
    else:
        print(2*p+1)
