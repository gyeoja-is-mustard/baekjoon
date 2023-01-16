N = int(input())
if N == 1:
    print(N)
else:
    for i in range(1,20000):
        if i*(i-1)/2 <= (N-2)//6 < i*(i+1)/2:
            print(i+1)
