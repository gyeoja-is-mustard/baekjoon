import sys

queue = []
n = int(input())
for i in range(n):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        num = order.split()[1] 
        queue.append(int(num))
    elif order == 'pop':
        if len(queue) == 0:
            print(-1)
        else: 
            print(queue[0])
            queue.pop(0)
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

        