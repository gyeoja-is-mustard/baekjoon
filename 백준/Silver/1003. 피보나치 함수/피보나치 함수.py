import sys

dic = {0:0, 1:1}
def fibonacci(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = fibonacci(n-1) + fibonacci(n-2) 
        return fibonacci(n-1) + fibonacci(n-2)

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        print(1, end = ' ')
        print(0)
    elif n == 1:
        print(0, end = ' ')
        print(1)
    else:
        print(fibonacci(n-1), end = ' ')
        print(fibonacci(n))
        
        
