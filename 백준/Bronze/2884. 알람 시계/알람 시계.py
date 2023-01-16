H, M = map(int,input().split())
if M >= 45:
    fM = M - 45
    print(H, fM)
else:
    fM = 15 + M
    if fM == 60:
        fM = 0
    if H == 0:
        fH = 23
    else: 
        fH = H - 1
    print(fH, fM)