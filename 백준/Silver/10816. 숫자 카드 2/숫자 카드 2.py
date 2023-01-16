import sys

ans = []

n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))

dic = {}
for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in m_list:
    if j in dic:
        ans.append(dic[j])
    else:
        ans.append(0)

for k in range(m):
    print(ans[k], end = ' ')