import sys

n = int(input())

list_num = []
for i in range(n):
    list_num.append(list(map(int, sys.stdin.readline().split())))

y_sorted_list = sorted(list_num, key = lambda x: x[1])
sorted_list = sorted(y_sorted_list, key = lambda x: x[0])

for j in range(n):
    print(f'{sorted_list[j][0]} {sorted_list[j][1]}')
    