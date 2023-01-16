import sys

n = int(input())
list = [int(sys.stdin.readline()) for i in range(n)]
list.sort()
for j in range(n):
    print(list[j])
