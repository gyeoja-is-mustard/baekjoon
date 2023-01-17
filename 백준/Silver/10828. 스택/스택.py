import sys

stack = []
n = int(input())
for i in range(n):
    order = sys.stdin.readline().strip()
    if 'push' in order:
        num = order.split()[1] 
        stack.append(int(num))
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else: 
            print(stack[-1])
            stack.pop()
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

        