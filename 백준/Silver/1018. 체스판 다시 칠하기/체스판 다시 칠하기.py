N, M = map(int,input().split())
a = []
c = []
fix = 0
for i in range(N):
    a.append(input())
for l in range(M-7):
    for j in range(N-7):
        for k in range(8):
            b = a[j+k]
            if (j+k) % 2 == 0:
                if b[l] == 'B':
                    fix += 1
                if b[l+1] == 'W':
                    fix += 1
                if b[l+2] == 'B':
                    fix += 1
                if b[l+3] == 'W':
                    fix += 1
                if b[l+4] == 'B':
                    fix += 1
                if b[l+5] == 'W':
                    fix += 1
                if b[l+6] == 'B':
                    fix += 1
                if b[l+7] == 'W':
                    fix += 1
            else:
                if b[l] == 'W':
                    fix += 1
                if b[l+1] == 'B':
                    fix += 1
                if b[l+2] == 'W':
                    fix += 1
                if b[l+3] == 'B':
                    fix += 1
                if b[l+4] == 'W':
                    fix += 1
                if b[l+5] == 'B':
                    fix += 1
                if b[l+6] == 'W':
                    fix += 1
                if b[l+7] == 'B':
                    fix += 1
        if fix >= 32:
            fix = 64 - fix
        c.append(fix)
        fix = 0
print(min(c))

