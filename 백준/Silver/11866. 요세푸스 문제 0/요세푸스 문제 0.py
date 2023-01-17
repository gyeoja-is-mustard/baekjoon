n, k = map(int, input().split())
num = [i for i in range(1, n+1)]
count = 0
index = 0
ans = []
while len(ans) < n:
    if num[index] != 0:
        count += 1
        if count == k:
            num[index] = 0
            count = 0
            ans.append(index+1)
        
    if index + 1 == n:
        index = 0
    else:
        index += 1
        
print("<" + ', '.join([str(ans[j]) for j in range(n)]) + ">")
        
