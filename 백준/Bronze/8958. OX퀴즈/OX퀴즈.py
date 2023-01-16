N = int(input())
score =[]
for i in range(N):
    A = input()
    B = A.split('X')
    C = list(map(len,B))
    score.append(sum(map(lambda n: int(n*(n+1)/2), C)))
for j in range(N):
    print(score[j])