import sys

n = int(input())

list = [0] * 10000

for i in range(n):
    input_num = int(sys.stdin.readline())
    list[input_num - 1] += 1
    
for j in range(10000):
    if list[j] != 0:
        for k in range(list[j]):
            print(j+1)
