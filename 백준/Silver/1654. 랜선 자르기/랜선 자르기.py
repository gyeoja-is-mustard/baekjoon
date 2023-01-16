K, N = map(int, input().split())
lines = []
for i in range(K):
    line = int(input())
    lines.append(line)
min, max = 1, max(lines)
while min <= max:
    mid = (min + max)//2
    cnt = 0
    for j in range(len(lines)):
        cnt += lines[j]//mid
    if cnt >= N:
        min = mid + 1
    else:
        max = mid - 1

print(max)