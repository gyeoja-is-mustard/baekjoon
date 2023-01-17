import sys
import math

n, m, b = map(int, sys.stdin.readline().split())
place = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
ans = math.inf
h = 0

for i in range(257):
    dig = 0
    put = 0
    for k in range(n):
        for l in range(m):
            if place[k][l] >= i:
                dig += place[k][l] - i           
            else:
                put += i - place[k][l]
        time = (dig*2) + put
    if dig + b >= put:
        if time <= ans:
            ans = time
            h = i
            
print(ans, h)