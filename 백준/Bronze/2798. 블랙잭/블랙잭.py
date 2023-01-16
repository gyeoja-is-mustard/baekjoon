n, m = map(int, input().split())
list = list(map(int, input().split()))
list_3 = []
for j in range(n):
    for k in range(j+1, n):
        for l in range(k+1, n):
            if list[j]+list[k]+list[l] <=m:
                list_3.append(list[j]+list[k]+list[l])
print(max(list_3))
            
