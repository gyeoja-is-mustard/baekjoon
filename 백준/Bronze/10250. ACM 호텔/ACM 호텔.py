t = int(input())
rl = []
for i in range(t):
    H, W, N = map(int,input().split())
    h = N%H
    if h == 0:
        h = H
    w = str(1+(N-1)//H)
    if len(w) < 2:
        w = '0'+ w
    rl.append(str(h)+w)
for j in range(t):
    print(rl[j])    