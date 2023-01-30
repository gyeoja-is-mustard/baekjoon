from collections import deque

def dfs(v):
    visit1[v] = 1
    print(v, end = ' ')
    for i in range(1, n + 1):
        if visit1[i] == 0 and graph[v][i] == 1:
            dfs(i)
            
def bfs(v):
    q = deque()
    q.append(v)
    visit2[v] = 1
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for i in range(1, n + 1):
            if visit2[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit2[i] = 1
    
n, m, v  = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

visit1 = [0] * (n + 1)
visit2 = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
dfs(v)
print()
bfs(v)